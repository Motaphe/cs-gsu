def swap_values(user_val1, user_val2, user_val3, user_val4):
    _user_val1 = user_val1
    user_val1 = user_val2
    user_val2 = _user_val1

    _user_val3 = user_val3
    user_val3 = user_val4
    user_val4 = _user_val3

    return (user_val1, user_val2, user_val3, user_val4)


def main():
    first = input("Enter first integer: ")
    second = input("Enter second integer: ")
    third = input("Enter third integer: ")
    fourth = input("Enter fourth integer: ")

    _first, _second, _third, _fourth = swap_values(first, second, third, fourth)
    print (f"Swapped: {_first} {_second} {_third} {_fourth}")

if __name__ == '__main__':
    main()





    