import requests
from bs4 import BeautifulSoup, Tag

from src.table import Table
from src.utils.logger import get_logger

logger = get_logger()
VOLLEYBALL_URL = "https://reboundibv.com.au/fixture"


class FixturePage:
    """
    Holds the contents of the Volleyball fixture HTML page.
    This class allows for dependency injection for testing. By default, it will make a HTTP request
    to get the contents.
    """

    def __init__(
        self, *, table_id: str = "tablepress-2", contents: str | bytes | None = None
    ) -> None:
        self._contents: str | bytes = contents if contents else self._request_content()
        self._table_id: str = table_id
        self._table: Table = self._get_html_table()

    # noinspection PyMethodMayBeStatic
    def _request_content(self) -> bytes:
        logger.info("Fetching HTTP Fixture content...")
        # noinspection SpellCheckingInspection
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            " AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/116.0.0.0 Safari/537.36"
        }
        response = requests.get(VOLLEYBALL_URL, headers=headers)

        if status_code := response.status_code != 200:
            raise Exception(
                f"Unexpected status code when making request to"
                f" {VOLLEYBALL_URL}. Status code: {status_code}."
                f" Content: {response.content}"
            )

        logger.info("Successfully fetched Fixture content")
        return response.content

    def _clean_text(self, text: str) -> str:
        return text.strip().replace("’", "'")

    # noinspection PyMethodMayBeStatic
    def _html_row_contents(self, html_row: Tag) -> list[any]:
        return [
            self._clean_text(html_column.text)
            for html_column in html_row.findAll(["th", "td"])
        ]

    def _get_html_table(self):
        soup = BeautifulSoup(self._contents, "html.parser")
        html_table = soup.find(id=self._table_id)
        html_rows = html_table.findAll("tr")
        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    def date(self) -> str:
        return self._table.cells[0][0]

    def _time(self, row: int) -> str:
        return self._table.row_heading(row)

    def team_time(self, team_name: str) -> str:
        row, _ = self._table.get_position_matching_str(team_name)
        return self._time(row)

    def court(self, team_name: str) -> str:
        _, column = self._table.get_position_matching_str(team_name)
        return self._table.column_heading(column)

    def opponent(self, team_name: str) -> str:
        row, column = self._table.get_position_matching_str(team_name)
        team_1, team_2 = self._table.cells[row][column].replace("\t", "").split("\nV\n")

        if team_name.lower() in team_1.lower():
            return team_2
        else:
            return team_1
