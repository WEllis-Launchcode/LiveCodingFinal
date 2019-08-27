from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keystream = 0
    encrypted = ""
    key.lower()
    for i in range(len(text)):
        keychar = keystream % len(key)
        if text[i] in lower_alphabet:
            new_char = rotate_character(text[i], alphabet_position(key[keychar]))
            new_char.lower()
            encrypted += new_char
            keystream += 1
        elif text[i] in upper_alphabet:
            new_char = rotate_character(text[i], alphabet_position(key[keychar]))
            new_char.upper()
            encrypted += new_char
            keystream += 1            
        else:
            encrypted += text[i]
    return encrypted

def main():
    text = input("Enter a text: ") 
    key = input("Enter a key: ") 
    print(encrypt(text, key))

if __name__ == "__main__":
    main()