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
    char **cell_letters = malloc(BOARD_SIZE * sizeof(char*));
    for (uint8_t i = 0; i < BOARD_SIZE * BOARD_SIZE; i++) {
        cell_letters[i] = malloc(strlen(letters[i]) * sizeof(char));
        cell_letters[i] = letters[i];
    }

    Board board = { .height = 4, .width = 4, .cells = cell_letters };
    print_board(board);
    free(cell_letters);
}
