from pathlib import Path
import pytest
from boggler.boggler_utils import read_boggle_file, BadBoardFormat

boards_path = Path(Path(__file__).parent.resolve())

@pytest.fixture(name="expected_board_4x4")
def fixture_expected_board_4x4():
    return [
        ['u', 'n', 'r', 'e'],
        ['qu', 'n', 'i', 'l'],
        ['i', 's', 'h', 'a'],
        ['s', 'e', 'l', 'b']
    ]

# Boards with clean input
@pytest.fixture(name="clean_4x4_path")
def fixture_clean_4x4_path():
    return Path(boards_path, "./boards/4x4_clean.board")

def test_clean_4x4_board(expected_board_4x4, clean_4x4_path):
    assert expected_board_4x4 == read_boggle_file(clean_4x4_path)


# Boards with leading whitespace
@pytest.fixture(name="leading_whitespace_4x4_path")
def fixture_leading_whitespace_4x4_path():
    return Path(boards_path, "./boards/4x4_leading_whitespace.board")

def test_leading_whitespace_4x4_board(expected_board_4x4, leading_whitespace_4x4_path):
    assert expected_board_4x4 == read_boggle_file(leading_whitespace_4x4_path)


# Boards with between whitespace
@pytest.fixture(name="between_whitespace_4x4_path")
def fixture_between_whitespace_4x4_path():
    return Path(boards_path, "./boards/4x4_between_whitespace.board")

def test_between_whitespace_4x4_board(expected_board_4x4, between_whitespace_4x4_path):
    assert expected_board_4x4 == read_boggle_file(between_whitespace_4x4_path)


# Boards with trailing whitespace
@pytest.fixture(name="trailing_whitespace_4x4_path")
def fixture_trailing_whitespace_4x4_path():
    return Path(boards_path, "./boards/4x4_trailing_whitespace.board")

def test_trailing_whitespace_4x4_board(expected_board_4x4, trailing_whitespace_4x4_path):
    assert expected_board_4x4 == read_boggle_file(trailing_whitespace_4x4_path)


# Boards with blank lines
@pytest.fixture(name="blank_lines_4x4_path")
def fixture_blank_lines_4x4_path():
    return Path(boards_path, "./boards/4x4_blank_lines.board")

def test_blank_lines_4x4_board(blank_lines_4x4_path):
    with pytest.raises(BadBoardFormat, match="must contain no blank lines"):
        read_boggle_file(blank_lines_4x4_path)


# Boards with inconsistent width lines
@pytest.fixture(name="inconsistent_width_4x4_path")
def fixture_inconsistent_width_4x4_path():
    return Path(boards_path, "./boards/4x4_inconsistent_width.board")

def test_inconsistent_width_4x4_board(inconsistent_width_4x4_path):
    with pytest.raises(BadBoardFormat, match="length of each row must be the same"):
        read_boggle_file(inconsistent_width_4x4_path)
