def read_file():
    with open("test.asm", 'r') as f:
        for line in f:
            print(line, end="")


if __name__ == "__main__":
    read_file()

    print("xo")