import urllib.parse

def encode_password(password):
    encoded_password = urllib.parse.quote(password, safe='')
    return encoded_password

def main():
    # Get the password from the user
    password = input("Enter your password: ")

    # Encode the password
    encoded_password = encode_password(password)

    # Print the encoded password
    print("Encoded Password:", encoded_password)

if __name__ == "__main__":
    main()

