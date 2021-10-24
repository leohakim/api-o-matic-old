from typing import List

import requests

from api_o_matic.bytes.models import Bit
from config import celery_app

URL_SCRAP_SERVICE = "http://vps.pesadoselnorte.com.ar:8001/"


@celery_app.task(
    default_retry_delay=30, max_retries=3, soft_time_limit=12000, time_limit=12000
)
def refresh_bits():
    """
    This function Request updated data and refresh the bits values
    """
    bits_updated = 0
    db = make_xpaths_bulk()
    for url, xpaths in db.items():
        updated_data = request_values(url, xpaths)
        for xpath, value in updated_data.items():
            matched = Bit.objects.active().filter(source__url=url, path=xpath)
            for _ in matched:
                _.value = value
                _.save()
                bits_updated += 1
                # todo Buscar una forma mas optima de updatear un bulk de registros de una sola vez

    return f"{bits_updated} bits updated."


def request_values(url: str, xpaths: List[str] = None) -> dict:
    """Make the POST Request and return the values"""
    data = {"url": url, "xpath": xpaths}
    response = requests.post(url=URL_SCRAP_SERVICE, json=data, timeout=12000)
    return response.json().get("data")


def make_xpaths_bulk() -> dict:
    """Query DB and return a bulk of URLs with XPATHS Array"""
    bits = Bit.objects.active().order_by("source")
    data = dict()
    for bit in bits:
        if bit.source.url in data:
            data[bit.source.url].append(bit.path)
        else:
            data.update({bit.source.url: [bit.path]})
    return data
