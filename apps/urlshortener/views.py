import string
import random

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.common.utils import response_200_ok, response_400_bad_request


class UrlShorternerView(APIView):

    def post(self, request: Request) -> Response:
        url = request.data.get("url")
        if not url:
            return response_400_bad_request(error="URL is missing")

        chars = string.ascii_letters + string.digits

        hash = "".join([random.choice(chars) for idx in range(7)])
        short_url = settings.URLSHORTENER_BASE_URL + hash

        return response_200_ok({"url": url, "short_url": short_url})

    def get(self, request: Request):
        short_url = request.query_params.get("short_url")
        if not short_url:
            return response_400_bad_request(error="Short URL is missing")
        
        return response_200_ok()
