from pprint import pprint

import pytest
import pytest_asyncio
from httpx import AsyncClient

import services
from config import Settings
from helper.event_hooks import log_request_event_hook, log_response_event_hook


@pytest_asyncio.fixture(scope="function")
async def pet(async_client):
    pets = services.Pets(async_client=async_client)
    pet = await pets.create_pet(payloads=pets.payloads.random_pet)
    yield pet
    await pets.delete_pet(pet_id=pet.id)


@pytest_asyncio.fixture(scope="function")
async def async_client() -> AsyncClient:
    config = Settings()
    return AsyncClient(
        timeout=config.api.timeout,
        base_url=config.api.host,
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook],
        },
    )
