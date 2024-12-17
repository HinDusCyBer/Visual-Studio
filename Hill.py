class HillCipher:
    def __init__(self):
        self.key = []
        self.plaintext = []
        self.encrypted_text = []
        self.m1 = 0
        self.n1 = 0
        self.m2 = 0
        self.n2 = 0

    def get_key(self):
        print("Enter rows and columns of matrix: ", end="")
        self.m1, self.n1 = map(int, input().split())
        print("Enter the key matrix:")
        for i in range(self.m1):
            row = list(map(int, input().split()))
            self.key.append(row)

    def display_key(self):
        print("Your key matrix is:")
        for i in range(self.m1):
            for j in range(self.n1):
                print(self.key[i][j], end="\t")
            print()

    def encrypt(self):
        temp = ""
        print("Enter rows and columns of matrix: ", end="")
        self.m2, self.n2 = map(int, input().split())
        if self.n1 == self.m2:
            print("Enter plaintext to encrypt:")
            for i in range(self.m2):
                row = list(map(int, input().split()))
                self.plaintext.append(row)

            print("Your plaintext is:")
            for i in range(self.m2):
                for j in range(self.n2):
                    print(self.plaintext[i][j], end="\t")
                print()

            for i in range(self.m1):
                row = []
                for j in range(self.n2):
                    encrypted_value = 0
                    for k in range(self.n1):
                        encrypted_value += self.key[i][k] * self.plaintext[k][j]
                    row.append(encrypted_value % 26)
                self.encrypted_text.append(row)

            print("Your encrypted text is:", end=" ")
            for i in range(self.m1):
                for j in range(self.n2):
                    temp += chr(self.encrypted_text[i][j] + 65)
            print(temp)
        else:
            print("Invalid input")

    def decrypt(self, encrypted_text, A):
        pass

    def transpose(self, A):
        temp = []
        for i in range(self.m1):
            row = []
            for j in range(self.n1):
                row.append(A[j][i])
            temp.append(row)
        return temp


def main():
    h1 = HillCipher()
    h1.get_key()
    h1.display_key()
    h1.encrypt()


if __name__ == "__main__":
    main()
