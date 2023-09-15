def main():
    for f in range(100):
        print("*", end="")
    print()

    for r in range(10):
        print("\t", end="")
    print("JADUAL DARAB")

    for f in range(100):
        print("*", end="")
    print()

    for y in range(1, 13):
        print("\t\t", y, end="")
    print("\n")

    for i in range(1, 13):
        print(i, "\t\t", end="")
        for j in range(1, 13):
            result = i * j
            print("", result, "", "\t", end="")
        print()


if __name__ == '__main__':
    main()
