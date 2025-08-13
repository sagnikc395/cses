#https://cses.fi/problemset/task/1068
#
def main():
    n = int(input())

    while(n != 1):
        curr = n
        print(curr,end=' ')
        if(n%2==0):
            n= n//2
        else:
            n = 3*n+1
    print(1,end='')
    
        

    

if __name__ == '__main__':
    main()
