from typing import Any

from bs4 import BeautifulSoup, Tag

from FixtureParser import FixtureParser
from Table import Table

# URL = "https://reboundibv.com.au/fixtures/"
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
# page = requests.get(URL, headers=HEADERS)
# soup = BeautifulSoup(page.content, "html.parser")
with open('mock_data/fixture_page.html', 'r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
html_table = soup.find(id="tablepress-2")
html_rows = html_table.findAll("tr")


def html_row_contents(html_row: Tag) -> list[Any]:
    html_columns = html_row.findAll(['th', 'td'])
    return [html_column.text.strip() for html_column in html_columns]


cells = [html_row_contents(html_row) for html_row in html_rows]
table = Table(cells)
parser = FixtureParser(table)

TEAM_NAME = "BAREFOOT"
message = f"This weeks game {parser.date()} at {parser.team_time(TEAM_NAME)} on court {parser.court(TEAM_NAME)}"

print("here")
