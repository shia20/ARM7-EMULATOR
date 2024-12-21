def read_file():
    code = []
    with open("test.asm", 'r') as f:
        for line in f:
            code.append(line)
    return code

if __name__ == "__main__":
    code = read_file()
    print(code)