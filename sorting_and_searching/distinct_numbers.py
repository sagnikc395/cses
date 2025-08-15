# https://cses.fi/problemset/task/1621

# import sys

# def main():
#     data = sys.stdin.buffer.read().split()
#     n = int(data[0])
#     numbers = list(map(int,data[1:1+n]))
#     print(len(set(numbers)))
    
# if __name__ == '__main__':
#     main()

# absolute fastest way

import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    seen = {}
    # using a dictionary based approach
    count = 0

    for num in data[1:1+n]:
        if num not in seen:
            seen[num] = True
            count += 1

    sys.stdout.write(str(count)+'\n')

if __name__ == '__main__':
    main()
            
