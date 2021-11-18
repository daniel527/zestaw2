def z4():
    allPossibilities = []

    print("Podaj x: ")
    x = int(input())
    print("Podaj y: ")
    y = int(input())
    print("Podaj z: ")
    z = int(input())
    print("Podaj n: ")
    n = int(input())

    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i + j + k != n:
                    allPossibilities.append([i,j,k])

    for element in allPossibilities:
        print(element)

if __name__ == '__main__':
    z4()
