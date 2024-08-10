#include <stdio.h>

int main() {
    char input;
    printf("Tell me something: ");
    scanf("%s", &input);
    printf("\nYou said, \"%s\"\n", &input);

    return 0;
}