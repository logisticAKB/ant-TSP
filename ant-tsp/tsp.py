from ant_algorithm import AntAlgorithm
from numpy import inf


row = [int(i) for i in input().split()]
n = len(row)
m = [row]
m[0][0] = inf
for i in range(n - 1):
    m.append([int(j) if int(j) != 0 else inf for j in input().split()])

ant_algorithm = AntAlgorithm(m, 100, 0.95, 1, 100, alpha=2.5, beta=2.5)
print(int(ant_algorithm.run()))
