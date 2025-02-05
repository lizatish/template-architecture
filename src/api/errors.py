from http import HTTPStatus

from fastapi import HTTPException


class CustomNotFound(HTTPException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'Custom element not found')

