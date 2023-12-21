from typing import Any

# noinspection PyProtectedMember
from bs4 import BeautifulSoup, Tag

from src.fixture_parser import FixtureParser
from src.table import Table
from src.volleyball_html_page import VolleyballHtmlPage


class MessageGenerator:
    """
    Given the volleyball fixture HTML page, derive the message with relevant information
    """

    def __init__(self):
        pass

    def generate_message(
        self, team_name: str, html_page: VolleyballHtmlPage | None = None
    ):
        html_page = html_page if html_page else VolleyballHtmlPage()
        table = self._html_page_to_table(html_page)
        parser = FixtureParser(table)

        return (
            f"This week's game {parser.date()} at {parser.team_time(team_name)}"
            f" on court {parser.court(team_name)}"
        )

    # noinspection SpellCheckingInspection
    def _html_page_to_table(self, html_page: VolleyballHtmlPage):
        soup = BeautifulSoup(html_page.contents, "html.parser")
        html_table = soup.find(id="tablepress-2")
        html_rows = html_table.findAll("tr")
        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    # noinspection PyMethodMayBeStatic
    def _html_row_contents(self, html_row: Tag) -> list[Any]:
        return [
            html_column.text.strip() for html_column in html_row.findAll(["th", "td"])
        ]
