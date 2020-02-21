'''Hashing is the concept of converting data of arbitrary size into data of fixed size.
A little bit more specifically, we are going to use this to turn strings (or possibly other data types) into integers.
This possibly sounds more complex than it is so let's look at an example. We want to hash the expression hello world, that is,
we want to get a numeric value that we could say represents the string.

By using the ord() function, we can get the ordinal value of any character.
For example, the ord('f') function gives 102. To get the hash of the whole string,
we could just sum the ordinal numbers of each character in the string:'''

a = sum(map(ord, 'world hello'))
#1116
b = sum(map(ord, 'gello xorld'))
#1116

print(a)
print(b)

#Perfect Hashing Function
def myhash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult*ord(ch)
        mult = mult +1
    return hv
for item in ('hello world', 'world hello', 'gello xorld'):
    print("{}: {}".format(item, myhash(item)))