import os

from src.message_generator import MessageGenerator
from src.pages.fixture_page import FixturePage
from src.pages.score_page import ScorePage


def _get_mock_fixture_page_content(file_name: str) -> str:
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    path_to_file = os.path.join(current_directory, f"mock_data/{file_name}")
    with open(path_to_file) as file:
        return file.read()


def test_message_generator_message():
    mock_fixture_page_content = _get_mock_fixture_page_content("fixture_page.html")
    mock_fixture_html_page = FixturePage(contents=mock_fixture_page_content)

    mock_score_page_content = _get_mock_fixture_page_content("score_page.html")
    mock_score_html_page = ScorePage(contents=mock_score_page_content)

    assert (
            MessageGenerator().generate_message(
                team_name="TICKLE TOES",
                fixture_page=mock_fixture_html_page,
                score_page=mock_score_html_page,
            )
            == "This week's game DATE: 27/02/24 at 7:30 PM on court 5.\n\nWe are currently placed 2nd.\n\nWe will be "
               "versing BAREFOOT BALLERS who are currently 1st."
    )
