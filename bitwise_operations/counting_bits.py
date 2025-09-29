#def count_set_bits(n):
    # using kernighan's algorithm
#    count = 0
#    while(n):
#        n &= (n-1)
#        count += 1
#    return count 
# TLE error in this, using a O(1) solution using set bits
#
# set_bits_table_256 = [0] * 256

# def init():
    # generate the lookup table
    # storin the count for all 8 but numbers
    # in count_set_bits , the 32bit numbers are divided
    # into 4 8-unit chunks and the table is used to quickly find the set bits
    # in each byte 
    # set_bits_table_256[0] = [0]

    # for i in range(256):
        # set_bits_table_256[i] = (i & 1) + set_bits_table_256[i//2]


# def count_set_bits(n):
    # return (set_bits_table_256[n & 0xff] +
    # set_bits_table_256[(n >> 8) & 0xff] +
    # set_bits_table_256[(n >> 16) & 0xff] +
    # set_bits_table_256[n >> 24])

    

def main():
    n = int(input())
    counter = 0
    # init()
    for i in range(1,n+1):
        counter += bin(i).count('1')
    print(counter)
        

if __name__ == '__main__':
    main()
