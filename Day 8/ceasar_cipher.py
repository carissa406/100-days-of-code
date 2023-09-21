alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")

print(art.logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    caesar(start_text = text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")



















#old code
""" def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            #print(f"og letter {alphabet.index(letter)}")
            #print(f"new letter {alphabet.index(letter) + shift}")
            if (alphabet.index(letter) + shift_amount) > 25:
                over_index = (alphabet.index(letter) + shift_amount) - 26
                cipher_text += alphabet[over_index]
            else:
                cipher_text += alphabet[alphabet.index(letter) + shift_amount]
    print(f"The encoded text is {cipher_text}")

#encrypt(text, shift)

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            #print(alphabet.index(letter) - shift)
            plain_text += alphabet[alphabet.index(letter) - shift_amount]
    print(f"The decoded text is {plain_text}")

#decrypt(text, shift)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("please input a valid option") """

