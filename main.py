def main():
    iternum = 0
    N = int(input('Enter the value for N: '))
    for i in range(N):
        for j in range(size(i)):
            print(f'({i}, {j})', end=' ')
            iternum += 1
        print()

    return iternum


if __name__ == '__main__':
    main()
