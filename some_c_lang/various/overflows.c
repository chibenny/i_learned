#include <stdio.h>
#include <string.h>


int main() {
    char mySolution[10] = "123456789";
    char myGuess[10];

    printf("guess: ");
    scanf("%9s", myGuess);

    printf("\nmyGuess: %s", myGuess);
    printf("\nmySolution: %s", mySolution);

    if (strcmp(myGuess, mySolution) == 0) {
        printf("\nSUCCESS!\n");
    } else {
        printf("\nFAIL!\n");
    }
};