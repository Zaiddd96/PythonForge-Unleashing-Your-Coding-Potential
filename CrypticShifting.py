import string
# from artt import caesar

# print(caesar)
def caesar_cipher(direction, shift, text):
    alphabet = " " + string.ascii_letters + string.punctuation + string.digits
    alpha = list(alphabet)
    end_text = ""

    for letter in text:
        position = alpha.index(letter)
        if direction == "decode":
            new_position = (position - shift) % len(alpha)
        else:
            new_position = (position + shift) % len(alpha)
        end_text += alpha[new_position]

    print(f"Your {direction}d text is: {end_text}")


while True:
    protocol = input("Type 'encode' to encrypt and 'decode' to decrypt and 'Q' to quit: ").lower()
    if protocol == "q":
        break
    else:
        plain_text = input("Enter your text: ")
        shift_no = int(input("Type the shift number: "))
        caesar_cipher(direction=protocol, shift=shift_no, text=plain_text)
