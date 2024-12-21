def read_file():
    code = []
    with open("test.asm", 'r') as f:
        for line in f:
            code.append(line)
    print(code)


if __name__ == "__main__":
    read_file()