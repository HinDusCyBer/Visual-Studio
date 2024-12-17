#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void encrypt(char *message, int shift) {
    char ch;
    for (int i = 0; message[i] != '\0'; i++) {
        ch = message[i];
        if (isalpha(ch)) {
            if (isupper(ch))
                message[i] = ((ch - 'A' + shift) % 26) + 'A';
            else
                message[i] = ((ch - 'a' + shift) % 26) + 'a';
        }
    }
}

void decrypt(char *message, int shift) {
    encrypt(message, 26 - (shift % 26));
}

int main() {
    char message[1000];
    int choice, shift;

    printf("Enter the message to encrypt or decrypt: ");
    fgets(message, sizeof(message), stdin);

    printf("Enter the shift value: ");
    scanf("%d", &shift);

    printf("Enter 1 to encrypt or 2 to decrypt: ");
    scanf("%d", &choice);

    if (choice == 1) {
        encrypt(message, shift);
        printf("Encrypted message: %s\n", message);
    } else if (choice == 2) {
        decrypt(message, shift);
        printf("Decrypted message: %s\n", message);
    } else {
        printf("Invalid choice. Please enter 1 to encrypt or 2 to decrypt.\n");
    }

    return 0;
}