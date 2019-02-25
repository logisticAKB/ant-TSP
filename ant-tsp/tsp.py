from ant_algorithm import AntAlgorithm


# Считываем матрицу
row = [int(i) for i in input().split()]
n = len(row)
m = [row]
for i in range(n - 1):
    m.append([int(j) for j in input().split()])

ant_algorithm = AntAlgorithm(m)
ant_algorithm.run()
