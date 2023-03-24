#ifndef BOGGLER_UTILS
#define BOGGLER_UTILS

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct Board {
    uint8_t height;
    unsigned short width;
    char **cells;
} Board;

char *get_cell_at(Board *board, uint8_t row, uint8_t col) {
    return board->cells[row * col + col];
}

int print_board(Board board) {
    char *row_delim = malloc((board.width * 4 + 1) * sizeof(char));
    row_delim[0] = '+';
    for (uint8_t i = 0; i < board.width; i++) {
        strcat(row_delim, "----");
    }
    row_delim[strlen(row_delim)-1] = '+';

    for (uint8_t row = 0; row < board.height; row++) {
        printf("%s\n", row_delim);
        for (uint8_t col = 0; col < board.width; col++) {
            printf("|%2s ", board.cells[(row * board.width) + col]);
        }
        puts("|");
    }
    printf("%s\n", row_delim);

    free(row_delim);

    return 0;
}

#endif
