def divide_apples(idx,arr,sum1,sum2,N):
    # if reached the end, return the difference
    if idx == N:
        return abs(sum1 - sum2)

    # choosing the current apple in grp1
    choice1 = divide_apples(idx + 1, arr, sum1+ arr[idx], sum2,N)

    # choosing the current applie in grp2
    choice2 = divide_apples(idx+1,arr,sum1,sum2+arr[idx],N)

    #min of both the choices return
    return min(choice1,choice2)


def main():
    n = int(input())
    weights = list(map(int,input().split(' ')))

    print(divide_apples(0,weights,0,0,n))
    

if __name__ == '__main__':
    main()
