#This challenge code or decode a message that you input
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '']

def get_Data():
    message = list(str(input("\nEnter a message: ").strip().lower()))
    number = int(input("Enter a number (1-26): "))
    while ((number >= 26) or (number <= 0)):
        number = int(input("\nOut of range... Try again: "))
    
    data = (message, number)
    return data

def make_Code(message, number):
    coded_message = ""
    for c in message:
        index_letter = alphabet.index(c)
        index_letter += number

        if (index_letter > 26):
            index_letter -= 27

        coded_message += alphabet[index_letter]
    
    print(f"\nThis is your coded message: {coded_message}\n")

def decode_Message(message, number):
    decoded_message = ""
    for c in message:
        index_letter = alphabet.index(c)
        index_letter -= number

        if (index_letter < 0):
            index_letter += 27
        
        decoded_message += alphabet[index_letter]
    
    print(f"\nThis is your decoded message: {decoded_message}\n")

def main():
    while True:
        option = int(input("""
    [1] Make a code
    [2] Decode a message
    [3] Quit
    Enter an option: """))

        match option:
            case 1:
                (message, number) = get_Data()
                make_Code(message, number)
                continue
            case 2:
                (message, number) = get_Data()
                decode_Message(message, number)
                continue
            case 3:
                print("\nShutting down...")
                break
            case _:
                print("\nThis option is not avaliable.\n")
                continue

main()