
def enum(string):
    index = string.rfind("10")
    if index == -1:
        print(string)
        return

    print(string)
    enum(string[:index] + string[index+1] + string[index] + string[index+2:])

if __name__ == "__main__":
    num = int(input())
    for i in range(num):
        [k, n] = [int(w) for w in input().split()]
        s = ""
        for i in range(n):
            s += "1"
        for j in range(k-n):
            s += "0"
        enum(s)
