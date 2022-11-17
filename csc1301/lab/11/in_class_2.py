

def feet_to_steps(user_feets):
    return user_feets//2.5


def main():
    print(
        f"Equivalent number of steps: {int(feet_to_steps(float(input('Number of feet walked: '))))}")


if __name__ == "__main__":
    main()
