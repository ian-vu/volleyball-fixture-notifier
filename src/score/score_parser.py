from dataclasses import dataclass

from src.table import Table
from src.utils.string_utils import int_to_position


@dataclass
class Score:
    position: int
    team_name: str
    score: int

    @property
    def position_nth(self):
        return int_to_position(self.position)


class ScoreParser:
    """Derive score data from table"""

    def __init__(self, table: Table):
        self._table = table

    def score(self, team_name: str) -> Score:
        team_row_index, _ = self._table.get_position_matching_str(team_name)
        team_row = self._table.cells[team_row_index]

        return Score(
            position=int(team_row[0]),
            team_name=team_name,
            score=team_row[2],
        )
