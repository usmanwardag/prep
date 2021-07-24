# https://www.youtube.com/watch?v=C4Kc8xzcA68
#
# Python list accesses every index at equal speed because
# it uses segments of RAM which are zero-indexed and are
# addressed by sequential integers.
#
# With Python dictionary (hash table), we can use keys instead 
# of indexes, and indexes can be almost anything.
#
# This means that in the ideal case, the lookup is constant time.
#
# A dictionary is really a list with every index storing hash, key,
# and value.
#
# Keys are hashed to produced indexes. E.g., in python, we can generate
# hash for a given key with hash().
#
# A hash should have these two properties: (i) it should scatter bits all
# around so that two very similar keys have very different hashes, and (ii)
# it should always generate the same hash for the same value.

for key in ['beta', 3.14, 3.14]:
    print(bin(hash(key)), key)

# Initially, Python starts with a hash table with a certain size 2^n.
# E.g., n=3.
#
# To locate an index, Python uses the bottom n bits of hash, and puts 
# an item there if it's not already there. 
#
# If an item is already there (collision), then it employs some maths 
# to locate another index, until it finds an empty slot.
#
# Therefore, at runtime, the lookup continues until Python finds an
# index whose 32-bit hash matches. 
#
# When deleting a key, we need to leave dummy keys, otherwise some keys
# may be lost.
#
# To keep collisions rare, dictionaries resize as soon as 2/3 of dictionary
# is filled.
#
# Suppose after the resizing, n=6. Therefore, now, the bottom six bits will
# be used to locate the index.
#
# On average, the collisions are very rare. 
