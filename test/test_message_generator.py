from MessageGenerator import MessageGenerator
from VolleyballHtmlPage import VolleyballHtmlPage


def test_message_generator_message():
    with open('mock_data/fixture_page.html', 'r') as file:
        mock_html_page_content = file.read()

    mock_html_page = VolleyballHtmlPage(mock_html_page_content)

    assert MessageGenerator().generate(mock_html_page) \
           == "This weeks game DATE: 29/08/23 at 6:45 PM on court 3"
