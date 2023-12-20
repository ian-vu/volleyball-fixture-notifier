Cell = str
Row = list[Cell]
Cells = list[Row]
Position = tuple[int, int]


class Table:
    def __init__(self, cells: Cells | None = None):
        self.cells: Cells = cells if cells is not None else []

    def get_position_matching_str(self, string: str) -> Position | None:
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if string.lower() in cell.lower():
                    return i, j

        raise NotFoundException(f"Unable to find {string} in table cells.")

    def row_heading(self, row_idx: int) -> Cell:
        if row_idx < 0 or row_idx >= self.num_rows():
            raise OutOfBoundsException(self, row_idx)

        return self._row_headings()[row_idx]

    def column_heading(self, column_idx: int) -> Cell:
        if column_idx < 0 or column_idx >= self.num_columns():
            raise OutOfBoundsException(self, column_idx)

        return self._column_headings()[column_idx]

    def num_rows(self) -> int:
        return len(self.cells)

    def num_columns(self) -> int:
        return len(self.cells[0])

    def _row_headings(self) -> Row:
        return [row[0] for row in self.cells]

    def _column_headings(self) -> Row:
        return self.cells[0]


class NotFoundException(Exception):
    pass


class OutOfBoundsException(Exception):
    def __init__(self, table: Table, idx: int):
        super().__init__(
            f"Out of bounds exception."
            f" Index: {idx} is not within table rows: {table.num_rows()}"
            f" or columns: {table.num_columns()}"
        )
