def backtracking(n,s):
    if n == 1:
        return s
    return [digit + bits for digit in backtracking(1,s)for bits in backtracking(n-1,s)]

print(backtracking(3,'abc'))

print([str(a)+str(b) for a in range(5)for b in range(5)])
