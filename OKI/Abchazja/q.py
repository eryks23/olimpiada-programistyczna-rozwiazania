line = input().split()
n = int(line[0])
m = int(line[1])
parent = list(range(n + 1))
components = n

def find(i):
    root = i

    while parent[root] != root:
        root = parent[root]

    while parent[i] != root:
        next_node = parent[i]
        parent[i] = root
        i = next_node
    return root

def connection(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_i] = root_j
        return True
    return False

for _ in range(m):
    u, v = map(int, input().split())

    if connection(u, v):
        components -= 1

print(components)