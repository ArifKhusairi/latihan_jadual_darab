def main():
    for i in range(55):
        print("*", end="")
    print()
    print("\t\t\t\t\t" + "JADUAL DARAB")
    for i in range(55):
        print("*", end="")
    print()

    for j in range(1,13):
        print("\t\t", j, end="")
    print("\n\n")

    num1 = 1
    result1 = 1
    for p in range(1,13):
        num1 = result1 * p
        print("\t\t", num1, end="")
    print("\n\n")

    num2 = 2
    result2 = 0
    num3 = 3
    result3 = 0
    for n in range(1,13):
        result2 = num2 * n
        print("\t\t", result2, end="")
    print("\n\n")

    for r in range(1,13):
        result3 = num3 * r
        print("\t\t", result3, end="")
    print("\n\n")

    for yahoo in range(1,13):
        print(yahoo, "\n")









if __name__ == '__main__':
    main()