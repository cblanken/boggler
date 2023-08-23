from __future__ import annotations


class BoardCell:
    """Boggle Board cell"""

    def __init__(
        self, row: int, col: int, letters: str, adjacent_cells: list[BoardCell] = None
    ) -> None:
        self.__row: int = row
        self.__col: int = col
        self.__pos: tuple[int, int] = (self.__row, self.__col)
        self.__letters: str = letters
        self.__adjacent_cells: list[BoardCell] = adjacent_cells

    @property
    def row(self) -> int:
        """Getter for row property"""
        return self.__row

    @property
    def col(self) -> int:
        """Getter for col property"""
        return self.__col

    @property
    def pos(self) -> tuple[int, int]:
        """Getter for pos property"""
        return self.__pos

    @property
    def letters(self) -> str:
        """Getter for letter property"""
        return self.__letters

    @property
    def adjacent_cells(self) -> list[BoardCell]:
        """Getter for adjacent_cells property"""
        return self.__adjacent_cells

    @adjacent_cells.setter
    def adjacent_cells(self, value):
        self.__adjacent_cells = value

    def __str__(self):
        return f"({self.__row}, {self.__col}): {self.__letters}"

    def __repr__(self):
        return f"(BoardCell({self.__row}, {self.__col}): {self.__letters}"


class BoggleBoard:
    """Boggle board structure"""

    def __init__(self, board: list[list[str]], max_word_len: int = 14) -> None:
        self.__height: int = len(board)
        self.__width: int = len(board[0]) if self.__height > 0 else 0
        self.__board_list = board
        self.__board: dict[tuple[int, int], BoardCell] = {}

        # Max word length is limited by size of the board
        self.__max_word_len = min(max_word_len, self.__width * self.__height)

        # Generate BoardCell for each position on the board
        for row in range(0, self.__height):
            for col in range(0, self.__width):
                self.__board[(row, col)] = BoardCell(row, col, board[row][col])

        # Update adjacent cell references for each BoardCell
        for cell in self.__board.values():
            adjacent_indexes = self.__get_adjacent_indexes(cell.row, cell.col)
            cell.adjacent_cells = [self.__board[(x[0], x[1])] for x in adjacent_indexes]

    def __str__(self):
        flattened_board_list = [y for x in self.__board_list for y in x]
        max_len = len(max(flattened_board_list, key=len))
        max_len = (
            max_len + 1 if max_len % 2 == 0 else max_len + 2
        )  # keep header_len odd
        header_len = self.__width * (max_len + 1) - 1
        head = "-" * header_len
        header = f"+{head}+\n"
        body = ""
        for row in self.__board_list:
            body += "|"
            for col in row:
                body += f"{col.upper(): ^{max_len}}|"
            body += "\n"
            body += header
        return f"{header}{body}"

    @property
    def height(self) -> int:
        """Getter for height property"""
        return self.__height

    @property
    def width(self) -> int:
        """Getter for width property"""
        return self.__width

    @property
    def max_word_len(self) -> int:
        """Getter for maximum word length property"""
        return self.__max_word_len

    @property
    def board(self) -> dict[tuple[int, int], BoardCell]:
        """Getter for board property"""
        return self.__board

    def __get_adjacent_indexes(self, row, col):
        """Return adjecency list for board of size `row x col`"""
        indexes = []
        if row > 0:
            indexes.append((row - 1, col))  # up
            if col > 0:
                indexes.append((row - 1, col - 1))  # up-left
            if col < self.width - 1:
                indexes.append((row - 1, col + 1))  # up-right
        if row < self.height - 1:
            indexes.append((row + 1, col))  # down
            if col > 0:
                indexes.append((row + 1, col - 1))  # down-left
            if col < self.width - 1:
                indexes.append((row + 1, col + 1))  # down-right
        if col > 0:
            indexes.append((row, col - 1))  # left
        if col < self.width - 1:
            indexes.append((row, col + 1))  # right
        return indexes

    def get_cell(self, row: int, col: int) -> BoardCell:
        """Return the value at the specified row x column"""
        return self.__board[(row, col)]
