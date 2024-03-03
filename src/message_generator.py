# noinspection PyProtectedMember

from src.pages.fixture_page import FixturePage
from src.pages.score_page import ScorePage


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
        score_page: ScorePage | None = None,
    ):
        fixture_page = fixture_page if fixture_page else FixturePage()
        score_page = score_page if score_page else ScorePage()

        opponent_name = fixture_page.opponent(team_name)
        opponent_score = score_page.score(opponent_name)
        team_score = score_page.score(team_name)

        return (
            f"This week's game {fixture_page.date()} at {fixture_page.team_time(team_name)}"
            f" on court {fixture_page.court(team_name)}.\n\n"
            f"We are currently placed {team_score.position_nth}.\n\n"
            f"We will be versing {opponent_score.team_name} who are currently {opponent_score.position_nth}."
        )
