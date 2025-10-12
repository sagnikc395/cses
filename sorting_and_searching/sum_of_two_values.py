def main():
    n , x = map(int,input().split(' '))
    arr = list(map(int,input().split(' ')))
    counter = {}

    found = False


    for i in range(0,n):
        if not found:
            if x - arr[i] in counter:
                print(counter[x-arr[i]] + 1 , i + 1)
                found = True
            counter[arr[i]] = i

    if not found:
        print("IMPOSSIBLE")

def find_two_sum(arr,target):
    arr = arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        summ = arr[left] + arr[right]
        if summ == target:
            return (left,right)

        elif summ < target:
            left += 1
        else:
            right -= 1

    return (-1,-1)

    

if __name__ == '__main__':
    #main()
    n , x = map(int,input().split(' '))
    arr = list(map(int,input().split(' ')))
    indices = find_two_sum(arr,x)

    if indices[0] != -1 and indices[1] != -1:
        print(indices[0],indices[1])
    else:
        print("IMPOSSIBLE")

        
