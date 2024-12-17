#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_valid_key(int key_matrix[3][3]) {
    int det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26;
    return det != 0 && __gcd(det, 26) == 1;
}

int* find_reverse_key(int key_matrix[3][3]) {
    int det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26;
    int mod_inv_det = pow(det, -1, 26);
    int adjugate[3][3] = {
        {key_matrix[1][1], -key_matrix[0][1], key_matrix[0][0]},
        {-key_matrix[1][0], key_matrix[0][0], key_matrix[1][1]},
        {key_matrix[0][1], -key_matrix[1][1], -key_matrix[0][0]}
    };
    int reverse_key_matrix[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            reverse_key_matrix[i][j] = (adjugate[i][j] * mod_inv_det) % 26;
        }
    }
    return reverse_key_matrix;
}

void encrypt(char* plaintext, int key_matrix[3][3]) {
    int encrypted_text[1024];
    for (int i = 0; i < strlen(plaintext); i += 2) {
        int row1 = plaintext[i] - 'A';
        int row2 = plaintext[i + 1] - 'A';
        encrypted_text[i] = ((key_matrix[0][0] * row1) + (key_matrix[0][1] * row2)) % 26 + 'A';
        encrypted_text[i + 1] = ((key_matrix[1][0] * row1) + (key_matrix[1][1] * row2)) % 26 + 'A';
    }
    printf("Encrypted: %s\n", encrypted_text);
}

void decrypt(char* ciphertext, int reverse_key_matrix[3][3]) {
    // Decrypt the ciphertext and print the result
    int decrypted_text[1024];
    for (int i = 0; i < strlen(ciphertext); i += 2) {
        int row1 = ciphertext[i] - 'A';
        int row2 = ciphertext[i + 1] - 'A';
        decrypted_text[i] = ((reverse_key_matrix[0][0] * row1) + (reverse_key_matrix[0][1] * row2)) % 26 + 'A';
        decrypted_text[i + 1] = ((reverse_key_matrix[1][0] * row1) + (reverse_key_matrix[1][1] * row2)) % 26 + 'A';
    }
    printf("Decrypted: %s\n", decrypted_text);
}

int main() {
    // Example key matrix (3x3 matrix)
    int key_matrix[3][3] = {
        {6, 24, 1},
        {13, 16, 10},
        {20, 17, 15}
    };
    // Check if the key matrix is valid
    if (is_valid_
