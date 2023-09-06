from typing import Any

from bs4 import BeautifulSoup, Tag

from FixtureParser import FixtureParser
from Table import Table
from VolleyballHtmlPage import VolleyballHtmlPage

TEAM_NAME = "BAREFOOT"


class MessageGenerator:
    def __init__(self):
        pass

    def generate(self, html_page: VolleyballHtmlPage | None = None):
        html_page = html_page if html_page else VolleyballHtmlPage()
        soup = BeautifulSoup(html_page.contents, 'html.parser')

        html_table = soup.find(id="tablepress-2")
        html_rows = html_table.findAll("tr")

        cells = [self._html_row_contents(html_row) for html_row in html_rows]
        table = Table(cells)
        parser = FixtureParser(table)

        return f"This weeks game {parser.date()} at {parser.team_time(TEAM_NAME)} on court {parser.court(TEAM_NAME)}"

    def _html_row_contents(self, html_row: Tag) -> list[Any]:
        return [html_column.text.strip() for html_column in html_row.findAll(['th', 'td'])]
