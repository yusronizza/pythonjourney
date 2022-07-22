alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(sentence, shift):
    length = len(sentence)
    encrypted = ""
    for i in range(0, length):
        if (sentence[i] in alphabet):
            position = alphabet.index(sentence[i])
            shifted = position + shift
            while (shifted > 25):
                shifted -= 26
            encrypted += alphabet[abs(shifted)]
        else:
            encrypted += sentence[i]
    return encrypted

def decrypt(sentence, shift):
    length = len(sentence)
    decrypted = ""
    for i in range(0, length):
        if (sentence[i] in alphabet):
            position = alphabet.index(sentence[i])
            reshifted = position - shift
            while (reshifted < 0):
                reshifted += 26
            decrypted += alphabet[reshifted]
        else:
            decrypted += sentence[i]
    return decrypted

def main():
    rerun = 'y'
    while rerun == 'y':
        menu = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if (menu == 'encode'):
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            result = encrypt(text, shift)
            print(result)
        if (menu == 'decode'):
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            result = decrypt(text, shift)
            print(result)
        rerun = input("Do you want to run the app again? (Y/y or N/n)\n")
main()