'''
Requirements for code:

Code was written in python 3.10.11
Matplotlib must be installed

'''


import random
import matplotlib.pyplot as plt

def ant_colony(item_list, no_bins, evap_rate, max_evals, paths, bpp):
    # create an empty 2d array to represent the construction graph
    c_graph = [[0 for i in range(0, no_bins)] for j in range(0, len(item_list))]

    # add random pheromone level for each item possibility
    for items in range(0, len(item_list)):  
        for bins in range(0, no_bins):
            c_graph[items][bins] = random.uniform(0,1)

    # create 2d array to contain bin contents
    bins = [[] for i in range(0, no_bins)]
    
    # create empty list to contain path of each ant
    ant_path = [[] for i in range(0, paths)]

    # create list to store fitnesses in
    fitness_list = []

    # total evaluations is set to 0
    tot_evals = 0
    # loop until the termination criteria is met
    while tot_evals < max_evals:
        # create p ant paths
        for p in range(0, paths):
            # randomly select a bin including the pheromone bias
            for item in range(0,len(item_list)-1):
                selected_bin = select_path(c_graph[item])
                ant_path[p].append(selected_bin)

                # add item index to the bin
                bins[selected_bin].append(item)

            # find fitness from bin and store in array
            weights = []
            for i in range(0, len(bins)):
                weights.append(bin_weight(bins[i], item_list))
            fitness = calculate_fitness(weights)
            
            fitness_list.append(fitness)

            # update the paths with pheromones
            c_graph_new = update_pheromones(c_graph, ant_path[p], fitness)
            
            # empty bins
            bins = [[] for i in range(0, no_bins)]

            # increase number of evaluations
            tot_evals = tot_evals+1
 
        # evaporate pheromones
        c_graph = evaporate_pheromones(evap_rate, c_graph_new)
        
        # reset stored ant paths
        ant_path = [[] for i in range(0, paths)]

        
    return fitness_list

# return a list containing the weight of each item in BPP1
def create_BPP1_items(no_items):
    item_list = [i for i in range(1, no_items+1)]
    
    return item_list

# return a list containing the weight of each item in BPP2
def create_BPP2_items(no_items):
    item_list = [(i**2)/2 for i in range(1, no_items+1)]
    
    return item_list

# returns a randomly selected path index from a list of pheromones
def select_path(pheromones):
    index_list = [[] for i in range(0, len(pheromones))]
    # create a list of the index numbers
    for i in range(0, len(pheromones)):
        index_list[i] = i
    
    # use the pheromones as weights to select a random index
    path = random.choices(index_list, weights=pheromones)
    #print("path: ", path)
    path_index = path[0]

    return path_index

# given list of pheromone values and selected path, update pheromones
def update_pheromones(p_values, path, fitness):
    for item in range (0, len(path)):
        p_values[item][path[item]] = p_values[item][path[item]] + (100/fitness)
    
    return p_values

# use the evaporation rate to remove pheromones from the paths
def evaporate_pheromones(e_rate, p_values):
    for i in range(0, len(p_values)):
        for j in range(0, len(p_values[i])):
            p_values[i][j] = p_values[i][j] * e_rate
    
    return p_values

# given a list containing the bin's items, calculate the weight
def bin_weight(bin_items , items_list):
    weight = 0
    for i in range(0, len(bin_items)):
        weight = weight + items_list[bin_items[i]]
    
    return weight

# calculate the fitness - difference between the heaviest and lightest bin
def calculate_fitness(bin_weights):
    fitness = 0
    
    # find max value in list
    max_val = max(bin_weights)
    
    # find min value in list
    min_val = min(bin_weights)
    
    # find difference
    fitness = max_val - min_val
    
    return fitness


# the following code completes the trials and plots the best result from each trial on a graph and inputs the best result from each trial into a table

print("BPP1:")
# trial 1
print("p = 100 and e = 0.90")
results = []
for i in range(1, 6):
    results.append(min(ant_colony((create_BPP1_items(500)), 10, 0.9, 10000, 100, 1)))
t1_results = results
bpp1_t1=  min(results)
print("Best fitness: ", min(results))

# trial 2
results = []
print("p = 100 and e = 0.60 ")
for i in range(1,6):
    results.append(min(ant_colony((create_BPP1_items(500)), 10, 0.6, 10000, 100,1)))
bpp1_t2=  min(results)
t2_results = results

print("Best fitness: ", min(results))

# trial 3
results = []
print("p = 10 and e = 0.90 ")
for i in range(1,6):
    results.append(min(ant_colony((create_BPP1_items(500)), 10, 0.9, 10000, 10,1)))
bpp1_t3=  min(results)
t3_results = results

print("Best fitness: ", min(results))

# trial 4
results = []
print("p = 10 and e = 0.60 ")
for i in range(1,6):
    results.append(min(ant_colony((create_BPP1_items(500)), 10, 0.6, 10000, 10,1)))
bpp1_t4=  min(results)
t4_results = results

print("Best fitness: ", min(results))

plt.plot([1,2,3,4], [bpp1_t1,bpp1_t2, bpp1_t3,bpp1_t4])
plt.grid()
plt.xlabel("Trial")
plt.ylabel("Fitness")
plt.savefig("BPP1", dpi=300)
plt.close()
table1_cols = ["p=100, e=0.90", "p=100, e=0.60", "p=10, e=0.90", "p=10, e=0.60"]
table1_rows = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]
table1_data = [
    [t1_results[0],t2_results[0],t3_results[0], t4_results[0]],
    [t1_results[1],t2_results[1],t3_results[1], t4_results[1]],
    [t1_results[2],t2_results[2],t3_results[2], t4_results[2]],
    [t1_results[3],t2_results[3],t3_results[3], t4_results[3]],
    [t1_results[4],t2_results[4],t3_results[4], t4_results[4]]
]

fig, ax = plt.subplots()

# Hide the axes
ax.axis("off")

table = plt.table(cellText=table1_data, rowLabels=table1_rows, colLabels=table1_cols)
plt.savefig("BPP1_table", bbox_inches="tight", dpi=300)
plt.close(fig)

plt.figure()
print("BPP2:")

# trial 1
results = []
print("p = 100 and e = 0.90")
for i in range(1, 6):
    results.append(min(ant_colony((create_BPP2_items(500)), 50, 0.9, 10000, 100,2)))
bpp2_t1=  min(results)
t1_results = results
plt.plot(1, min(results))

# trial 2
results = []
print("p = 100 and e = 0.60 ")
for i in range(1,6):
    results.append(min(ant_colony((create_BPP2_items(500)), 50, 0.6, 10000, 100,2)))
bpp2_t2=  min(results)
t2_results = results
plt.plot(2,min(results))

# trial 3
results = []
print("p = 10 and e = 0.90 ")
for i in range(1,6):
    results.append(min(ant_colony((create_BPP2_items(500)), 50, 0.9, 10000, 10,2)))
bpp2_t3=  min(results)
t3_results = results
plt.plot(3,min(results))

# trial 4
results = []
print("p = 10 and e = 0.60 ")
for i in range(1,6):
    results.append(min(ant_colony((create_BPP2_items(500)), 50, 0.6, 10000, 10,2)))
bpp2_t4=  min(results)
t4_results = results
plt.plot(4,min(results))


plt.plot([1,2,3,4], [bpp2_t1,bpp2_t2, bpp2_t3,bpp2_t4])

plt.grid()
plt.xlabel("Trial")
plt.ylabel("Fitness")
plt.savefig("BPP2", dpi=300)
plt.close()

table2_cols = ["p=100, e=0.90", "p=100, e=0.60", "p=10, e=0.90", "p=10, e=0.60"]
table2_rows = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]
table2_data = [
    [t1_results[0],t2_results[0],t3_results[0], t4_results[0]],
    [t1_results[1],t2_results[1],t3_results[1], t4_results[1]],
    [t1_results[2],t2_results[2],t3_results[2], t4_results[2]],
    [t1_results[3],t2_results[3],t3_results[3], t4_results[3]],
    [t1_results[4],t2_results[4],t3_results[4], t4_results[4]]
]

fig, ax = plt.subplots()

# Hide the axes
ax.axis("off")

table = plt.table(cellText=table2_data, rowLabels=table2_rows, colLabels=table2_cols)
plt.savefig("BPP2_table",bbox_inches="tight", dpi=300)

plt.close(fig)



table3_cols = ["BPP1", "BPP2"]
table3_rows = ["p=100, e=0.90", "p=100, e=0.60", "p=10, e=0.90", "p=10, e=0.60"]
table3_data = [
    [bpp1_t1, bpp2_t1],
    [bpp1_t2, bpp2_t2],
    [bpp1_t3, bpp2_t3],
    [bpp1_t4, bpp2_t4]
]

fig, ax = plt.subplots()

# Hide the axes
ax.axis("off")

table = plt.table(cellText=table3_data, rowLabels=table3_rows, colLabels=table3_cols)
plt.savefig("result_table",bbox_inches="tight", dpi=300)

plt.close(fig)

