import os
from dotenv import load_dotenv


load_dotenv()


# PROJECT #
DJANGO_SECRET_KEY: str = os.getenv("DJANGO_SECRET_KEY")


# URL SHORTENER #
URLSHORTENER_BASE_URL: str = os.getenv("URLSHORTENER_BASE_URL")

