from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup, Tag

from src.table import Table
from src.utils.logger import get_logger
from src.utils.string_utils import int_to_position

logger = get_logger()


@dataclass
class Score:
    position: int
    team_name: str
    score: int

    @property
    def position_nth(self):
        return int_to_position(self.position)


class ScorePage:
    """
    Holds the contents of the Volleyball score HTML page.
    This class allows for dependency injection for testing. By default, it will make a HTTP request
    to get the contents.
    """

    _URL: str = "https://reboundibv.com.au/scores/"

    def __init__(
        self, *, table_id: str = "tablepress-26", contents: str | bytes | None = None
    ):
        self._contents = contents if contents else self._request_content()
        self._table_id = table_id
        self._table = self._get_html_table()

    # noinspection PyMethodMayBeStatic
    def _get_html_table(self):
        soup = BeautifulSoup(self._contents, "html.parser")
        html_table = soup.find(id=self._table_id)
        html_rows = html_table.findAll("tr")
        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    def _html_row_contents(self, html_row: Tag) -> list[any]:
        return [
            html_column.text.strip() for html_column in html_row.findAll(["th", "td"])
        ]

    # noinspection PyMethodMayBeStatic
    def _request_content(self) -> str | bytes:
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

    def score(self, team_name: str) -> Score:
        team_row_index, _ = self._table.get_position_matching_str(team_name)
        team_row = self._table.cells[team_row_index]

        return Score(
            position=int(team_row[0]),
            team_name=team_name,
            score=team_row[2],
        )
