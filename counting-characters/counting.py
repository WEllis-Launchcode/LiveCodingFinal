x = input("Enter a sentence: ")


num_alphabet = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,;.:?!-'...''()/[]"

letter_count = {} 
for char in x:
    if char in num_alphabet:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()

for char in keys:
    print(char, letter_count[char])
