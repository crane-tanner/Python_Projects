from art import logo

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in ALPHABET:
            position = ALPHABET.index(char)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % 26
            else:
                new_position = (position - shift_amount) % 26
            end_text += ALPHABET[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

def main():
    print(logo)
    
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %= 26
        
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if answer == 'no':
            should_continue = False
            print("Goodbye")

if __name__ == "__main__":
    main()