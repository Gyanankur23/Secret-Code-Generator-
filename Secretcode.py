# Secret Code Generator - Caesar Cipher Style

def encode_message(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char  # Keep non-letter characters as is
    return result

def decode_message(message, shift):
    return encode_message(message, -shift)  # Decoding is just negative shift

def show_menu():
    print("\nSecret Code Generator")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            message = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter shift value (e.g., 2): "))
                encoded = encode_message(message, shift)
                print("Encoded message:", encoded)
            except ValueError:
                print("Please enter a valid number for shift.")
        
        elif choice == '2':
            message = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter shift value used during encoding: "))
                decoded = decode_message(message, shift)
                print("Decoded message:", decoded)
            except ValueError:
                print("Please enter a valid number for shift.")
        
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the program
main()
