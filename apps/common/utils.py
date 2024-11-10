from typing import Union

from rest_framework import status
from rest_framework.response import Response


def response_200_ok(data: Union[dict, None] = None) -> Response:
    response = dict()
    if not data:
        data = {"message": "success"}
    response.update(data)
    return Response(data, status=status.HTTP_200_OK)


def response_400_bad_request(error: str) -> Response:
    data = {
        "errors": error
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)