import numpy as np
from numpy.random import choice as np_choice


class AntAlgorithm():
    def __init__(self, matrix, t_max, q, r, n_ants, alpha=1, beta=1):
        """
        :param matrix (2D array): Square matrix of distances. Diagonal is assumed to be numpy.inf
        :param t_max (int): Number of iterations.
        :param q (int): The order value of the optimal solution.
        :param r (int): Pheromone evaporation rate.
        :param n_ants (int): Number of ants.
        :param alpha (int/float): When α = 0, the choice of the nearest city is most likely.
        :param beta (int/float): When β = 0, the selection occurs only on the basis of pheromone.
        """
        self.matrix = np.array(matrix)
        self.pheromone = np.ones(self.matrix.shape) / len(matrix)
        self.n = len(self.matrix)
        self.t_max = t_max
        self.q = q
        self.r = r
        self.n_ants = n_ants
        self.alpha = alpha
        self.beta = beta
        self.shortest_path = np.inf

    def run(self):
        """
        :return (float): Weight of the shortest path.
        """
        for t in range(self.t_max):
            new_paths = []
            for ant in range(self.n_ants):
                new_path = self.get_new_path()
                new_paths.append(new_path)

            self.shortest_path = min(self.shortest_path, min(new_paths))

            for i in range(self.n):
                for j in range(self.n):
                    self.spread_pheromone(i, j, new_paths)
        return self.shortest_path

    def get_new_path(self):
        """
        :return (float): Weight of the new path.
        """
        path = 0
        for i, j in self.new_path():
            path += self.matrix[i][j]
        return path

    def new_path(self):
        """
        :return (1D array of tuples): New path transitions.
        """
        path = []
        start = 0
        visited = set()
        prev = start
        visited.add(start)
        for i in range(self.n - 1):
            next = self.pick_next(self.pheromone[prev], self.matrix[prev], visited)
            path.append((prev, next))
            visited.add(next)
            prev = next
        path.append((prev, start))
        return path

    def spread_pheromone(self, i, j, new_paths):
        """
        :param i (int): Current row.
        :param j (int): Current column.
        :param new_paths (2D array): Array of all new paths.
        """
        s = 0
        for p in new_paths:
            s += (self.q / p)
        self.pheromone[i][j] = (1 - self.r) * self.pheromone[i][j] + s

    def pick_next(self, prev_pheromone, prev_row, visited):
        """
        :param prev_pheromone (1D array): Previous row of the matrix of pheromone.
        :param prev_row (1D array): Previous row of the matrix of distances.
        :param visited (set): Set of visited nodes.
        :return (int): Next node by using probability.
        """
        row_pheromone = np.copy(prev_pheromone)
        row_pheromone[list(visited)] = 0

        row = row_pheromone ** self.alpha * ((1.0 / prev_row) ** self.beta)
        norm_row = row / row.sum()

        next = np_choice(range(self.n), 1, p=norm_row)[0]

        return next
