## using the property of XOR
#
def graycode(n):
    result = []

    for i in range(1 << n):
        gray = i ^ (i >> 1)
        code = ""
        for j in range(n-1,-1,-1):
            code += '1' if (gray & (1 << j)) else '0'
        result.append(code)

    return result

def main():
    n = int(input())
    res = graycode(n)
    for r in res:
        print(r)

if __name__ == '__main__':
    main()
        
