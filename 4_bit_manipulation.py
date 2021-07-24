# https://www.youtube.com/watch?v=5J4rWJHwLSE

x = 4

# Print binary representation
print(bin(x))

x = 0b11001011
y = 0b10101101

# Bitwise AND
print((x & y) == 0b10001001)
# Bitwise OR
print((x | y) == 0b11101111)
# Bitwise XOR (if either is one, but not both)
print((x ^ y) == 0b01100110)
# Bitwise not (actually not because integers in Python are signed)
print(x, ~x, bin(~x))
print(~x, ~(~x), bin(~(~x)))


# Bitwise left shift - move all bits to left
# A left shift effectively adds a zero bit to the end
# i.e., multiplies the number by 2
x = 0b1101
print(x, bin(x), x << 1, bin(x << 1))
print(x, bin(x), x << 2, bin(x << 2))


# Bitwise right shift - move all bits to right
# i.e., discard the last bit
x = 0b1101
print(x, bin(x), x >> 1, bin(x >> 1))
print(x, bin(x), x >> 2, bin(x >> 2))
