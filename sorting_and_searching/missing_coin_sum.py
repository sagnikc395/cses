def missingCoins(coins):
    coins.sort()

    val = 1
    for i in coins:
        if i > val:
            return val
        val += i

    return val

    
if __name__ == '__main__':
    n = int(input())
    coins = list(map(int,input().split(' ')))
    print(missingCoins(coins))
