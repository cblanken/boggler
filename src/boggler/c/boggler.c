#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "board.h"

int main(int argc, char **argv) {
    const uint8_t BOARD_SIZE = 4;
    char *letters[] = {
        "u", "n", "r", "e",
        "qu","n", "i", "l",
        "i", "s", "h", "a",
        "s", "e", "l", "b"
    };
    char **cell_letters = malloc(BOARD_SIZE * sizeof(struct BoardCell*));

    struct BoardCell **cells = malloc(sizeof(struct BoardCell*) * BOARD_SIZE * BOARD_SIZE);
    for (uint8_t i = 0; i < BOARD_SIZE * BOARD_SIZE; i++) {
        cells[i] = create_board_cell(letters[i], (int)(i / BOARD_SIZE), i % BOARD_SIZE);
    }

    Board board = { .height = 4, .width = 4, .cells = cells };
    print_board(&board);
    free(cell_letters);
}
