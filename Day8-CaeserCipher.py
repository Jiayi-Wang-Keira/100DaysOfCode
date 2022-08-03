alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(in_text, in_shift, in_direction):
    # adjust the shift
    in_shift = in_shift % 26

    # body
    new_text = ""
    for char in in_text:
        if char in alphabet:
            loc = alphabet.index(char)
            if in_direction == "encode":
                new_loc = loc + in_shift
                if new_loc > 25:
                    new_loc -= 26
            elif in_direction == "decode":
                new_loc = loc - in_shift
                if new_loc < 0:
                    new_loc += 26
            new_text += alphabet[new_loc]
        else:
            new_text += char
    print(f"The {in_direction} text is {new_text}")

conti='yes'
while conti=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)

    conti = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
else:
    print("goodbye")

