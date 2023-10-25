# Daniel Hernandez
def encode(password):
    return int(password) + int('3'*len(password))

#Oliver's Decode
def decode(password):
    list= []
    decode = ''
    for i in str(password):
        list.append(i)
    for digit in list:
        if digit == '1':
            decode += '8'
        elif digit == '2':
            decode += '9'
        elif digit == '0':
            decode +='7'
        else:
            decode += str(int(digit)-3)
    return decode
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
        if user_action == '2':
            print("The encoded password is", password, "and the original password is" , decode(password))
        if user_action == '3':
            break


if __name__ == "__main__":
    main()
