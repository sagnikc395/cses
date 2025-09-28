import math

#def factorial(n):
    #fac = 1

    #for i in range(2,n+1):
    #    fac = fac * i

    #return fac
    #return math.factorial(n)   

def factorial(N):
    f = 1

    for i in range(2,N+1):
        f *= i

    return f


def trailing_zeros(n):
    fact = factorial(n)
    count = 0

    while(fact%10 ==0):
        count += 1
        fact = fact // 10

    return count 



def main():
    n = int(input())
    print(trailing_zeros(n))

if __name__ == '__main__':
    main()  
