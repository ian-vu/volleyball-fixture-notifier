from Table import Table


class FixtureParser:
    def __init__(self, table: Table):
        self._table = table

    def date(self) -> str:
        return self._table.cells[0][0]

    def _time(self, row: int) -> str:
        return self._table.row_heading(row)

    def team_time(self, team_name: str) -> str:
        row, _ = self._table.get_position_matching_str(team_name)
        return self._time(row)

    def court(self, team_name: str) -> str:
        _, column = self._table.get_position_matching_str(team_name)
        return self._table.column_heading(column)
