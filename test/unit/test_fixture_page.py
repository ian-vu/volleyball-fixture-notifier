from src.fixture_page import FixturePage
import os


def _get_mock_html_page_content(file_name: str) -> str:
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    path_to_file = os.path.join(current_directory, f"mock_data/{file_name}")
    with open(path_to_file) as file:
        return file.read()


mock_html_content = _get_mock_html_page_content("fixture_page.html")
mock_fixture_page = FixturePage(contents=mock_html_content)


def test_date():
    assert mock_fixture_page.date() == "DATE: 27/02/24"


def test_team_time():
    assert mock_fixture_page.team_time("BAREFOOT") == "7:30 PM"
    assert mock_fixture_page.team_time("SITUATION") == "6:45 PM"
    assert mock_fixture_page.team_time("BAREFOOT") == "7:30 PM"


def test_court():
    assert mock_fixture_page.court("BAREFOOT") == "5"
    # noinspection SpellCheckingInspection
    assert mock_fixture_page.court("BAMYAN") == "3"


def test_opponent():
    assert mock_fixture_page.opponent("BAREFOOT") == "TICKLE TOES"
    assert mock_fixture_page.opponent("LONG DROP") == "BEAUTY + THE BEAST"
