#include <stdio.h>
#include <string.h>

void vulnerableFunction() {
    char buffer[50];
    printf("Enter your input: ");
    gets(buffer);  // Dangerous, but perfect for the demo
    printf("You entered: %s\n", buffer);
}

int main() {
    vulnerableFunction();
    printf("Function executed successfully.\n");
    return 0;
}