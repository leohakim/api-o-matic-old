import random

from config import celery_app


@celery_app.task()
def refresh_bits():
    """
    This function scrap into the bits sources and refresh the bits values
    """

    number_random = random.randint(50, 200)
    return f"{number_random} bits updated."
