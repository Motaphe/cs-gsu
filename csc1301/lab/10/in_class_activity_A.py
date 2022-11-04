def exact_change(cents):

    if cents == 0:
        return "no change"

    else:
        quarter = cents // 25
        rem1 = cents % 25
        dime = rem1 // 10
        rem2 = rem1 % 10
        nickel = rem2 // 5
        rem3 = rem2 % 5
        penny = rem3

        return penny, nickel, dime, quarter


def main():
    input_val = int(input("Cents: "))
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    to_print = {}

    if num_pennies == 0:
        pass
    elif num_pennies == 1:
        to_print["penny"] = num_pennies
    else:
        to_print["pennies"] = num_pennies

    if num_nickels == 0:
        pass
    elif num_nickels == 1:
        to_print["nickel"] = num_nickels
    else:
        to_print["nickels"] = num_nickels

    if num_dimes == 0:
        pass
    elif num_dimes == 1:
        to_print["dime"] = num_dimes
    else:
        to_print["dimes"] = num_dimes

    if num_quarters == 0:
        pass
    elif num_quarters == 1:
        to_print["quarter"] = num_quarters
    else:
        to_print["quarters"] = num_quarters

    for denomination in to_print:
        print(f"{to_print[denomination]} {denomination}")


if __name__ == "__main__":
    main()






