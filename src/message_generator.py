from typing import Any

# noinspection PyProtectedMember
from bs4 import BeautifulSoup, Tag

from src.fixture_page import FixturePage
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
        fixture_page: FixturePage | None = None,
        score_html_page: ScoreHtmlPage | None = None,
    ):
        fixture_page = fixture_page if fixture_page else FixturePage()

        score_html_page = score_html_page if score_html_page else ScoreHtmlPage()
        score_parser = ScoreParser(self._score_html_page_to_table(score_html_page))

        team_score = score_parser.score(team_name)
        opponent_score = score_parser.score(fixture_page.opponent(team_name))

        return (
            f"This week's game {fixture_page.date()} at {fixture_page.team_time(team_name)}"
            f" on court {fixture_page.court(team_name)}.\n\n"
            f"We are currently placed {team_score.position_nth}.\n\n"
            f"We will be versing {opponent_score.team_name} who are currently {opponent_score.position_nth}."
        )

    def _score_html_page_to_table(self, score_html_page: ScoreHtmlPage) -> Table:
        soup = BeautifulSoup(score_html_page.contents, "html.parser")
        html_table = soup.find(id="tablepress-26")
        html_rows = html_table.findAll("tr")

        cells = [self._html_row_contents(html_row) for html_row in html_rows]

        return Table(cells)

    def _html_row_contents(self, html_row: Tag) -> list[Any]:
        return [
            html_column.text.strip() for html_column in html_row.findAll(["th", "td"])
        ]
