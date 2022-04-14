if __name__ == '__main__':
    y = 7
    x = 7
    for i in range(1, y):
        if i == 1 or i == y - 1:
            print("*" * i)
            continue

        for j in range(1, x - 1):
            if j == 1:
                print("*", end="")
                continue
            elif j == i:
                print("*")
                break
            print(" ", end="")
