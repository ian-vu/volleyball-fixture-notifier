import os

from MessageGenerator import MessageGenerator
from VolleyballHtmlPage import VolleyballHtmlPage


def get_mock_fixture_page_content():
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    path_to_file = os.path.join(current_directory, "mock_data/fixture_page.html")
    with open(path_to_file) as file:
        return file.read()


def test_message_generator_message():
    mock_html_page_content = get_mock_fixture_page_content()
    mock_html_page = VolleyballHtmlPage(mock_html_page_content)

    assert (
        MessageGenerator().generate_message(
            team_name="I DON’T LIKE SAND", html_page=mock_html_page
        )
        == "This week's game DATE: 29/08/23 at 6:45 PM on court 4"
    )
