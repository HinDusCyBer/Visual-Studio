import numpy as np

def is_valid_key(key_matrix):
    det = int(np.linalg.det(key_matrix)) % 26
    return det != 0 and np.gcd(det, 26) == 1

def find_reverse_key(key_matrix):
    det = int(np.linalg.det(key_matrix)) % 26
    mod_inv_det = pow(det, -1, 26)
    adjugate = np.linalg.inv(key_matrix) * det
    reverse_key_matrix = (adjugate % 26) * mod_inv_det
    return reverse_key_matrix.astype(int)

def encrypt(plain_text, key_matrix):
    encrypted_text = []
    for i in range(0, len(plain_text), len(key_matrix)):
        segment = plain_text[i:i+len(key_matrix)]
        segment_vector = [ord(c) - ord('A') for c in segment]
        product = np.dot(key_matrix, segment_vector) % 26
        encrypted_text.extend([chr(val + ord('A')) for val in product])
    return ''.join(encrypted_text)

def decrypt(cipher_text, reverse_key_matrix):
    decrypted_text = []
    for i in range(0, len(cipher_text), len(reverse_key_matrix)):
        segment = cipher_text[i:i+len(reverse_key_matrix)]
        segment_vector = [ord(c) - ord('A') for c in segment]
        product = np.dot(reverse_key_matrix, segment_vector) % 26
        decrypted_text.extend([chr(val + ord('A')) for val in product])
    return ''.join(decrypted_text)

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

if is_valid_key(key_matrix):
    reverse_key_matrix = find_reverse_key(key_matrix)
    plaintext = "HELLO"
    
    encrypted_text = encrypt(plaintext, key_matrix)
    print("Encrypted:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, reverse_key_matrix)
    print("Decrypted:", decrypted_text)
else:
    print("Invalid key matrix")
