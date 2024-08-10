/*
int         (4 bytes) | %d for printing
double      (8 bytes) | %lf for printing
float       (4 bytes) | %f for printing
char        (1 byte)  | %c for printing
*/

#include <stdio.h>

int main() {
    int number;
    double decimal;
    float floating;
    char character;

    for (int i = 0; i < 4; i++) {
        switch (i) {
            case 0:
                printf("Size of int: %zu\n", sizeof (number));
                break;
            case 1:
                printf("Size of double: %zu\n", sizeof(decimal));
                break;
            case 2:
                printf("Size of float: %zu\n", sizeof(floating));
                break;
            case 3:
                printf("Size of char: %zu\n", sizeof(character));
                break;
        }
    }

    return 0;
}