import requests
from bs4 import BeautifulSoup
from lxml import etree

from api_o_matic.bytes.models import Bit
from config import celery_app

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/94.0.4606.61 Safari/537.36"
}


@celery_app.task()
def refresh_bits():
    """
    This function scrap into the bits sources and refresh the bits values
    """
    bits = Bit.objects.active().order_by("source")
    last_url, dom = None, None
    bits_updated = 0
    for bit in bits:
        url = bit.source.url
        xpath = bit.path
        if url != last_url:
            webpage = requests.get(url=url, headers=HEADERS, timeout=2)
            soup = BeautifulSoup(webpage.content, "html.parser")
            dom = etree.HTML(str(soup))
            last_url = url
        if dom is not None:
            value = dom.xpath(xpath)[0].text
            if value:
                bits_updated += 1
                bit.value = value
                bit.save()

    return f"{bits_updated} bits updated."
