def laps_to_miles(user_laps):
    return user_laps * 0.25

if __name__ == "__main__":
    print (f"{laps_to_miles(float(input('Enter the number of laps: '))):.2f}")




