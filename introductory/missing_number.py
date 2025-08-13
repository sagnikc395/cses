# https://cses.fi/problemset/task/1083


def main():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    sum1 = n*(n+1)//2
    sum2 = sum(arr)
    print(abs(sum1-sum2))

if __name__ == '__main__':
    main()
