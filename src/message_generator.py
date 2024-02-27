from typing import Any

# noinspection PyProtectedMember
from bs4 import BeautifulSoup, Tag

from src.fixture.fixture_html_page import FixtureHtmlPage
from src.fixture.fixture_parser import FixtureParser
from src.score.score_html_page import ScoreHtmlPage
from src.score.score_parser import ScoreParser
from src.table import Table


class MessageGenerator:
    """
    Given the volleyball fixture HTML page, derive the message with relevant information
    """

    def __init__(self):
        pass

    def generate_message(
        self,
        team_name: str,
        fixture_html_page: FixtureHtmlPage | None = None,
        score_html_page: ScoreHtmlPage | None = None,
    ):
        fixture_html_page = (
            fixture_html_page if fixture_html_page else FixtureHtmlPage()
        )
        fixture_parser = FixtureParser(
            self._fixture_html_page_to_table(fixture_html_page)
        )

        score_html_page = score_html_page if score_html_page else ScoreHtmlPage()
        score_parser = ScoreParser(self._score_html_page_to_table(score_html_page))

        team_score = score_parser.score(team_name)
        opponent_score = score_parser.score(fixture_parser.opponent(team_name))

        return (
            f"This week's game {fixture_parser.date()} at {fixture_parser.team_time(team_name)}"
            f" on court {fixture_parser.court(team_name)}.\n\n"
            f"We are currently placed {team_score.position_nth}.\n\n"
            f"We will be versing {opponent_score.team_name} who are currently {opponent_score.position_nth}."
        )

    # noinspection SpellCheckingInspection
    def _fixture_html_page_to_table(self, fixture_html_page: FixtureHtmlPage) -> Table:
        soup = BeautifulSoup(fixture_html_page.contents, "html.parser")
        html_table = soup.find(id="tablepress-2")
        html_rows = html_table.findAll("tr")
        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    def _score_html_page_to_table(self, score_html_page: ScoreHtmlPage) -> Table:
        soup = BeautifulSoup(score_html_page.contents, "html.parser")
        html_table = soup.find(id="tablepress-26")
        html_rows = html_table.findAll("tr")

        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    # noinspection PyMethodMayBeStatic
    def _html_row_contents(self, html_row: Tag) -> list[Any]:
        return [
            html_column.text.strip() for html_column in html_row.findAll(["th", "td"])
        ]
