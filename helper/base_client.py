from typing import Any

import allure
from httpx import AsyncClient, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

from config import Settings, settings
from .event_hooks import log_request_event_hook, log_response_event_hook

from .helper import Helper


class BaseClient(Helper):
    def __init__(self, async_client: AsyncClient):
        self.async_client = async_client

    @allure.step("Make GET request to {url}")
    async def get(
        self,
        url: URL | str,
        headers: Any,
        params: QueryParams | None = None,
    ) -> Response:
        return await self.async_client.get(url, headers=headers, params=params)

    @allure.step("Make POST request to {url}")
    async def post(
        self,
        url: URL | str,
        headers: Any,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        return await self.async_client.post(
            url, headers=headers, json=json, data=data, files=files
        )

    @allure.step("Make PATCH request to {url}")
    async def patch(
        self,
        url: URL | str,
        headers: Any,
        json: Any | None = None,
    ) -> Response:
        return await self.async_client.patch(url, headers=headers, json=json)

    @allure.step("Make DELETE request to {url}")
    async def delete(
        self,
        url: URL | str,
        headers: Any,
    ) -> Response:
        return await self.async_client.delete(url=url, headers=headers)
