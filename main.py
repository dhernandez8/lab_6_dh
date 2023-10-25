# Daniel Hernandez
def encode(password):
    return int(password) + int('3'*len(password))


def main():
    password = ''
    while True:
        user_action = input(f'Menu\n'
                            f'{"-"*13}\n'
                            f'1. Encode\n'
                            f'2. Decode\n'
                            f'3. Quit\n'
                            f'\n'
                            f'Please enter an option: ')
        if user_action == '1':
            password = encode(input(f"Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        if user_action == '3':
            break


if __name__ == "__main__":
    main()
