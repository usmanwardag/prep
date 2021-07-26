# Why do we need 2's complement?
# https://www.youtube.com/watch?v=lKTsv6iVxV4
#
# Two's complement is used to store signed numbers.
#
# How should be store signed numbers in bits?
# One idea is to assign the highest bit 0 or 1
# depending on whether the number is +ve or -ve.
#
# This idea has two problems. 
# 1- There are two numbers to store 0 (1000 and 0000). 
# 2- We can't use binary operations to add, multiply etc!
#
# To address these problems, we can use two's complement
# format of representing signed numbers.
#
# The intuitive idea behind two's complement is that if
# we have 2^N space, then the upper half stores negative
# and the lower half positive numbers.
#
# Concretely, the two's complement of an N-bit number is 
# defined as its complement with respect to 2^N, i.e., the 
# sum of a number and its two's complement is 2^N.
#
# Two's complement is achived by (i) reversing bits, and 
# (ii) adding 1.
#
# With this representation, we can perform binary operations
# as normal, and we have a single representation for zero.


def twos_complement(num, N):
    if num == 0:
        return 0
    else:
        return (1 << N) - num


def recover_twos_complement(num, N):
    # Check if signed bit (highest bit) is set
    if (num & (1 << N-1)):
        return num - (1 << N)
    else:
        return num


num = 5
N = 3
print(num, twos_complement(num, N))
assert num + twos_complement(num, N) == pow(2, N)

print(0, twos_complement(0, 3))
assert 0 == twos_complement(0, 3)

num = 5
N = 4

print(num, twos_complement(num, N), recover_twos_complement(twos_complement(num, N), N))
assert recover_twos_complement(twos_complement(num, N), N) == -num
