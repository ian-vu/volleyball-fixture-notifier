from src.fixture.fixture_parser import FixtureParser
from src.table import Table

# noinspection SpellCheckingInspection
mock_table = Table(
    [
        ["DATE: 29/08/23", "1", "2", "3", "4", "5", "6"],
        [
            "6:45 PM",
            "YOURS, MINE, SORRY!\nV\nBLOCK PARTY",
            "JERRY + HUDO\nV\nDAVID + GOLIATH",
            "BAREFOOT BALLERS\nV\nBIG SITUATION",
            "SERVES YOU RIGHT\nV\nI DON’T LIKE SAND",
            "",
            "",
        ],
        [
            "7:30 PM",
            "APPA YIP YIP\nV\nBAMYAN",
            "QUICK FINISHERS\nV\nSOMETIMES GOOD AND SHIT",
            "THE SOLI-MEN\nV\nHOES",
            "PORK BELLY BOIS\nV\nTEAM PLS",
            "",
            "",
        ],
        [
            "8:15 PM",
            "DIG, SET, LOSE\nV\nHOW I SET YOUR MOTHER",
            "TIGHT + DRY\nV\nF.I.",
            "BRENTWOOD RANGERS\nV\nSUPER SPIKE BROS",
            "GOLD DIGGERS\nV\nBALLBUSTERS",
            "",
            "",
        ],
    ]
)

mock_fixture_parser = FixtureParser(mock_table)


def test_date():
    assert mock_fixture_parser.date() == "DATE: 29/08/23"


def test_team_time():
    assert mock_fixture_parser.team_time("BAREFOOT") == "6:45 PM"
    assert mock_fixture_parser.team_time("SITUATION") == "6:45 PM"
    assert mock_fixture_parser.team_time("APPA") == "7:30 PM"
    assert mock_fixture_parser.team_time("QUICK") == "7:30 PM"


def test_court():
    assert mock_fixture_parser.court("BAREFOOT") == "3"
    # noinspection SpellCheckingInspection
    assert mock_fixture_parser.court("BAMYAN") == "1"
