from httpx import Request, Response

from utils.logger import get_logger

logger = get_logger("HTTP_CLIENT")


async def log_request_event_hook(request: Request):
    logger.info(f"Make {request.method} request to {request.url}")


async def log_response_event_hook(response: Response):
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )
