# Ant algorithm for travelling salesman problem

This program finds the shortest possible route that visits every city exactly once and returns to the starting point.

# Algorithm
- Entering the distance matrix.
- Initialization of pheromone concentration.
- Initialization of algorithm parameters: `t_max`, `q`, `r`, `n_ants`, `α`, `β`.
- Initialization of the shortest route as `infinity`.
- For each iteration:
    - For each ant:
        - Build the routes and calculate weight using the following formula:
        
            ![equation](https://latex.codecogs.com/gif.latex?P_%7Bij%7D%3D%5Cfrac%7B%5Ctau_%7Bij%7D%5E%7B%5Calpha%20%7D%28%5Cfrac%7B1%7D%7Bd_%7Bij%7D%7D%29%5E%7B%5Cbeta%20%7D%7D%7B%5Csum_%7Bj%5Cin%20allowed%20nodes%7D%5Ctau_%7Bij%7D%5E%7B%5Calpha%20%7D%28%5Cfrac%7B1%7D%7Bd_%7Bij%7D%7D%29%5E%7B%5Cbeta%20%7D%7D), where
            
            ![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20_%7Bij%7D%28t%29) - pheromone level,
            ![equation](https://latex.codecogs.com/gif.latex?d%20_%7Bij%7D) - distance between i and j,
            ![equation](https://latex.codecogs.com/gif.latex?%5Calpha%20%2C%5Cbeta) - constants.
    - Check all new routes for new shortest one.
    - For each edge:
    
        - Update the pheromone on the edge using the following formula:
        
            ![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20_%7Bij%7D%28t&plus;1%29%3D%281-%5Crho%20%29%5Ctau%20_%7Bij%7D%28t%29&plus;%5Csum_%7Bk%5Cin%20colonyThatUsedEdge%28i%2Cj%29%7D%5Cfrac%7BQ%7D%7BL_%7Bk%7D%7D)
- Print weight of the shortest rote.  

# Instruction
- Run `tsp.py`.
- Enter matrix of distances, diagonal is assumed to be 0.

    For example: 


   ![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%200%20%26%202%20%26%2030%20%26%201%20%26%20%5C%5C%204%20%26%200%20%26%2047%20%26%207%20%26%20%5C%5C%2031%20%26%2033%20%26%200%20%26%2036%20%26%20%5C%5C%2020%20%26%2013%20%26%2016%20%26%2028%20%26%20%5C%5C%209%20%26%2036%20%26%2022%20%26%200%20%26%20%5Cend%7Bpmatrix%7D)
- Enjoy your result!
