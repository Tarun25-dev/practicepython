"""
Question 1: Task Scheduling

A system manages a list of tasks, where each task has a priority and the time required to complete it.

You are given "N" tasks.

Each task has:

"priority" (smaller value = higher priority)

"time" required to complete the task

Sort the tasks based on:

Ascending order of priority

If priorities are the same, sort by ascending time

Important: Use Selection Sort to perform the sorting.

Input Format:

First line: integer "N"

Next "N" lines: two integers "priority" and "time"

Output Format:

Print sorted tasks ("priority time")

Sample Input:

5

1 10

2 5

1 5

3 7

2 3

Sample Output:

1 5, 1 10, 2 3, 2 5, 3 7

Question 2: Minimum Cost to Connect Cities with Server Cost

You are given:

"N" cities labeled from "1" to "N"

"M" bidirectional roads, each with a cost

An array "serverCost[]" where each city has a server maintenance cost

You must:

Connect all cities such that every city is reachable from any other city with minimum total road cost

Find the second minimum cost to connect all cities using a different set of roads

Total Cost = Sum of selected road costs + Sum of all server costs

Input Format:

First line: two integers "N M"

Next "M" lines: three integers "u v w"

Last line: "N" integers representing "serverCost"

Output Format:

Print two integers:

Minimum total cost

Second minimum total cost

Constraints:

If it is not possible to connect all cities(disjoint graph), print "-1 -1"

If second minimum spanning tree does not exist, print minimum cost and "-1"

Sample Input:

4 5

1 2 1

2 3 2

3 4 3

1 4 4

1 3 5

10 20 30 40

Sample Output:

106 107
"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px = find(parent, x)
    py = find(parent, y)
    
    if px == py:
        return False
    
    if rank[px] < rank[py]:
        parent[px] = py
    else:
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
    return True


def kruskal(n, edges, skip_edge_index=-1):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    cost = 0
    count = 0
    used_edges = []
    
    for i, (u, v, w) in enumerate(edges):
        if i == skip_edge_index:
            continue
        
        if union(parent, rank, u, v):
            cost += w
            count += 1
            used_edges.append(i)
    
    if count != n - 1:
        return float('inf'), []
    
    return cost, used_edges


# Input
n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

serverCost = list(map(int, input().split()))

# Sort edges
edges.sort(key=lambda x: x[2])

# Step 1: MST
mst_cost, mst_edges = kruskal(n, edges)

if mst_cost == float('inf'):
    print("-1 -1")
else:
    # Step 2: Second MST
    second_mst = float('inf')
    
    for edge_index in mst_edges:
        cost, _ = kruskal(n, edges, edge_index)
        second_mst = min(second_mst, cost)
    
    server_sum = sum(serverCost)
    
    min_total = mst_cost + server_sum
    
    if second_mst == float('inf'):
        print(min_total, -1)
    else:
        print(min_total, second_mst + server_sum)
