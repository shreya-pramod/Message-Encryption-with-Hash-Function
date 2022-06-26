
randomConstant = [3963322530, 2719440241, 2631015465]
initial_vector = 3284486410

def hashFunc(messageBlock, key):
    funcSum = "0"
    for obj in randomConstant:
        funcSum = key ^ int(messageBlock, 2)
        funcSum = funcSum ^ obj
        key = funcSum
    return funcSum


def findOrd(input_msg):
    ord_list = []
    for letter in input_msg:
        ord_list.append(ord(letter))
    return ord_list


def readFile(filename):
    file = ""
    with open(filename) as f:
        for words in f.readlines():
            file = file + words
    return file


def decToBin(input_list):
    result = []
    for val in input_list:
        result.append(bin(val)[2:])
    return result


def main():
    input_msg = readFile("inputFile.txt")
    ord_val = findOrd(input_msg)
    binVal = decToBin(ord_val)
    finVal = ""

    for val in binVal:
        finVal = finVal + val
    if len(finVal) % 32 != 0:
        while len(finVal) % 32 != 0:
            finVal = finVal + "0"

    values = [finVal[i:i + 32] for i in range(0, len(finVal), 32)]
    blockSum = "0"
    for i in range(0, len(values)):
        if i == 0:
            message = hashFunc(values[i], initial_vector)
            blockSum = initial_vector ^ message
        else:
            message = hashFunc(values[i], blockSum)
            blockSum = blockSum ^ message

    print("The output for " + '"' + input_msg + '"' + " is: " + bin(blockSum)[2:])


if __name__ == '__main__':
    main()
