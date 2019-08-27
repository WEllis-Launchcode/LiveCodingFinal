from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ""
    for ch in range(len(text)):
        encrypted += rotate_character(text[ch], int(rot))
    return encrypted  

def main():
    text = input("Enter a text: ")
    rot = input("Enter a number to rotate: ")
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()