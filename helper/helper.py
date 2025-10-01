from config import settings


class Helper:

    headers = {"Content-Type": "application/json"}
    host: str = settings.api.host
