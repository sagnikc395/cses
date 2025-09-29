def generate_permutations(s,path=""):
    # base case -> string is empty , yield the
    # current permutation
    if not s:
        yield path

    # recursive case: loop thorugh each character in the string
    for i in range(len(s)):
        yield from generate_permutations(s[:i] + s[i+1:],path + s[i])



def main():
    s = input()
    items = set(sorted(list(generate_permutations(s))))
    print(len(items))
    for item in items:
        print(item)

if __name__ == '__main__':
    main()
