#include <stdio.h>
#include <string.h>

struct DataType {
    char name[20];
    char description[100];
    char printFormat[3];
    int sizeInBytes;
};

int main() {
    struct DataType dataTypes[5] = {
        {"int", "Represents an integer. e.g. 4", "%d", sizeof(int)},
        {"double", "Represents a higher-precision floating point number", "%lf", sizeof(double)},
        {"float", "Represents a lower-precision floating point number", "%f", sizeof(float)},
        {"char", "Character", "%c", sizeof(char)}
    };

    struct DataType manualDataType;
    manualDataType.sizeInBytes = 4;
    strcpy(manualDataType.name, "manual");
    strcpy(manualDataType.description, "This is a manual data type constructed outside of an array of initializers ({})");
    strcpy(manualDataType.printFormat, "%d");

    dataTypes[4] = manualDataType;

    printf("The size of `dataTypes` is: %lu\n\n", sizeof(dataTypes));

    int lenDataTypes = sizeof(dataTypes) / sizeof(dataTypes[0]);
    // NTS: sizeof(dataTypes) returns the size of the array in bytes
    // When used in a loop `for (int i = 0; i < sizeof(dataTypes); i++)` we get a leak!

    for (int i = 0; i < lenDataTypes; i++) {
        printf("Type: %s", dataTypes[i].name);
        printf("\nAbout %s: %s", dataTypes[i].name, dataTypes[i].description);
        printf("\nPrint format: %s", dataTypes[i].printFormat);
        printf("\nSize in bytes: %d\n\n", dataTypes[i].sizeInBytes);
    };

    return 0;
};