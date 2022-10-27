def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return miles_driven / miles_per_gallon * dollars_per_gallon
    
if __name__ == "__main__":
    miles_per_gallon = float(input("Enter the miles per gallon: "))
    dollars_per_gallon = float(input("Enter the dollars per gallon: "))
    miles_driven = float(input("Enter the miles driven: "))
    print (f"Gas cost: ${driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):.2f}")








