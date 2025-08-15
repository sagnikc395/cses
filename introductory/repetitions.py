# https://cses.fi/problemset/task/1069
#
def main():
    s = input()
    # iterate through that stores the character of the current substring
    # if the char at the ith iteration changes we update this variable
    # else we increment the current count.
    # at each iteration, we also update the answer to be max(answer,count)
    current = ''
    count = 0
    ans = 0
    for i in range(0,len(s)):
        if s[i] != current:
            current = s[i]
            count = 0
        if s[i] == current:
            count += 1

        ans = max(ans,count)

    print(ans)
    
    
if __name__ == '__main__':
    main()
