from typing import Any

from bs4 import BeautifulSoup, Tag

from FixtureParser import FixtureParser
from Table import Table
from VolleyballHtmlPage import VolleyballHtmlPage

TEAM_NAME = "BAREFOOT"


class MessageGenerator:
    """
    Given the volleyball fixture HTML page, derive the message with relevant information
    """

    def __init__(self):
        pass

    def generate_message(self, html_page: VolleyballHtmlPage | None = None):
        html_page = html_page if html_page else VolleyballHtmlPage()
        table = self._html_page_to_table(html_page)
        parser = FixtureParser(table)

        return f"This week's game {parser.date()} at {parser.team_time(TEAM_NAME)}" \
               f" on court {parser.court(TEAM_NAME)}"

    def _html_page_to_table(self, html_page: VolleyballHtmlPage):
        soup = BeautifulSoup(html_page.contents, 'html.parser')
        html_table = soup.find(id="tablepress-2")
        html_rows = html_table.findAll("tr")
        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    def _html_row_contents(self, html_row: Tag) -> list[Any]:
        return [html_column.text.strip() for html_column in
                html_row.findAll(['th', 'td'])]
