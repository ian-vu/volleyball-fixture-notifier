import requests

from src.utils.logger import get_logger

logger = get_logger()


class ScoreHtmlPage:
    """
    Holds the contents of the Volleyball score HTML page.
    This class allows for dependency injection for testing. By default, it will make a HTTP request
    to get the contents.
    """

    _URL: str = "https://reboundibv.com.au/scores/"

    def __init__(self, contents: str | None = None):
        self.contents: str = contents if contents else self._request_content()

    # noinspection PyMethodMayBeStatic
    def _request_content(self) -> str:
        logger.info("Fetching HTTP content...")
        # noinspection SpellCheckingInspection
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            " AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/116.0.0.0 Safari/537.36"
        }
        response = requests.get(self._URL, headers=headers)

        if status_code := response.status_code != 200:
            raise Exception(
                f"Unexpected status code when making request to"
                f" {self._URL}. Status code: {status_code}."
                f" Content: {response.content}"
            )

        logger.info("Successfully fetched Score content")
        return response.content
