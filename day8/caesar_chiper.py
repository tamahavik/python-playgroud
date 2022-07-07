alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt , type 'decode' to decrypt: \n")
text = input("Type your message:\n").lower()
shift = int(input('Type the shift number:\n'))


# def encrypt(text_encrypt, text_shift):
#     message = ""
#     for txt in text_encrypt:
#         index = alphabet.index(txt)
#         new_index = index + text_shift
#         if new_index >= len(alphabet) - 1:
#             new_index -= len(alphabet)
#         message += alphabet[new_index]
#     print(message)
#
#
# def decrypt(text_decrypt, text_shift):
#     message = ""
#     for txt in text_decrypt:
#         index = alphabet.index(txt)
#         new_index = index - shift
#         if new_index < 0:
#             new_index += len(alphabet)
#         message += alphabet[new_index]
#     print(message)


def caesar(text_message, shift_amount, direction_inp):
    message = ""
    for letter in text_message:
        index = alphabet.index(letter)
        new_index = None
        if direction_inp == "encode":
            new_index = index + shift_amount
            if new_index > len(alphabet):
                new_index -= len(alphabet)
        elif direction_inp == "decode":
            new_index = index - shift_amount
            if new_index < 0:
                new_index += len(alphabet)
        message += alphabet[new_index]
    print(message)


caesar(text, shift, direction)
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
