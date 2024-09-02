// Worked from https://youtu.be/KJgsSFOSQv0?si=hi39QzlFYkxEFePJ

#include <stdlib.h>


int main() {

    int secretNumber = 5;
    int guess;

    while(guess != secretNumber) {
        printf("Enter a number: ");
        scanf("%d", &guess);
    }

    return 0;
};