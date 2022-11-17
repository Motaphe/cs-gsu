

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    for _ in miles_driven:
        print(
            f"Gas cost for {_} miles: ${_/miles_per_gallon * dollars_per_gallon:.2f}")


def main():
    miles_per_gallon = float(input("Miles per gallon? "))
    dollars_per_gallon = float(input("Dollars per gallon? $"))
    driving_cost(miles_per_gallon, dollars_per_gallon,
                 miles_driven=[10, 50, 400])


if __name__ == "__main__":
    main()
