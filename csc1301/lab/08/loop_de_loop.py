def makelist(num):
    return [i for i in range(num)]

def rocketcountdown(num):
    lst = [i for i in range(num, 0, -1)]
    lst.append("We have lift off!")
    return lst

def doubleloop(num1, num2):
    return [f"{i}:{j}" for i in range(num1) for j in range(num2)]
    
def main():
    print (makelist(10))
    print (makelist(3))

    print (rocketcountdown(10))
    print (rocketcountdown(2))

    print (doubleloop(3, 3))
    print (doubleloop(3, 4))

if __name__ == "__main__":
    main()