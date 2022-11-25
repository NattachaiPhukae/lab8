OKGREEN = '\033[92m'
OKCYAN = '\033[96m'
WARNING = '\033[93m'
ENDC = '\033[0m'
data = [29, 10, 14, 37, 14, 20, 7, 16, 12]


def PrintColorData(data, i, j):
    for index, value in enumerate(data):
        if i-j > 1 and index == i-1:
            print(OKCYAN + str(value) + ENDC, end=' ')
        elif index == j:
            print(OKGREEN + str(value) + ENDC, end=" ")
        elif index == i:
            print(WARNING + str(value) + ENDC, end=" ")
        else:
            print(value, end=" ")
    print()


def LomutoQuicksort(data, start, end):
    if start < end:
        pivot = LomutoPartition(data, start, end)
        LomutoQuicksort(data, start, pivot - 1)
        LomutoQuicksort(data, pivot + 1, end)


def LomutoPartition(data, start, end):
    if start-end == 1:
        return
    pivot = data[end]
    i = end
    j = start
    while j < i:
        PrintColorData(data, i, j)
        if data[j] < pivot:
            j += 1
        elif data[j] >= pivot:
            if i-j > 1:
                data[i], data[i-1] = data[i-1], data[i]
            data[i], data[j] = data[j], data[i]
            i -= 1

    PrintColorData(data, i, j)
    print()
    return i


print("Original array:", data)
print()
LomutoQuicksort(data, 0, len(data) - 1)
print("Sorted Array", data)