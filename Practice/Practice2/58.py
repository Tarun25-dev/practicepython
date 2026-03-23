# the king wants to rank N soldiers using ranks 1 to r.
# rule1: No two adjacent soldiers can have the same rank.
# rule2: the first soldiers rank is always 1.
# rule3: the last soldiers rank must be L.
# goal: Find the no.of valid sequences.

# Example: N=4, r=4, L=4 then output will be count of ways to place 1 _ _ L o/p: 7

def countWays(N,r,L):
    count = 0

    def backtrack(pos,arr):
        nonlocal count

        if pos == N:
            if arr[-1] == L:
                count += 1
            return
        for i in range(1, r+1):
            if i != arr[-1]:
                arr.append(i)
                backtrack(pos + 1,arr)
                arr.pop()
    backtrack(1,[1])
    return count

N = 4
r = 4
L = 4
print(countWays(N,r,L))