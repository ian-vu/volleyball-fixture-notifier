import requests

VOLLEYBALL_URL = "https://reboundibv.com.au/fixture"


class VolleyballHtmlPage:
    def __init__(self, contents: str | None = None):
        self.contents = contents if contents else self._request_content()

    def _request_content(self) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                          " AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/116.0.0.0 Safari/537.36"}
        response = requests.get(VOLLEYBALL_URL, headers=headers)

        if status_code := response.status_code != 200:
            raise Exception(f"Unexpected status code when making request to"
                            f" {VOLLEYBALL_URL}. Status code: {status_code}."
                            f" Content: {response.content}")

        return response.content
