#Getting the input from cosole
nodes_number=int(input('Enter the number of the nodes '))

nodes_paths=[]
for node in range(nodes_number):
    node_paths=[]
    for counter in range(nodes_number):
        if(counter==node):
            node_paths.append(0)

        else:
            node_paths.append(int(input('enter the path costs from  node'+ str(node+1) +  ' to node'+str(counter+1)+'--> ')))

    nodes_paths.append(node_paths)
    print('-------------------------------------------------------------------------------------  ')

target_node=int(input('which node you want to compute the shortest path from it  '))-1


############################### Implemting the algorithm ##########################################
shortest_cost=nodes_paths[target_node]
shortest_path=[]

taken_nodes=dict()
for counter in range(nodes_number):
    taken_nodes[str(counter)]=shortest_cost[counter]


#the first step for the target node
for counter in range(len(shortest_cost)):
    if (shortest_cost[counter]!=999):
        shortest_path.append('from '+str(target_node+1)+'to ---> '+str(counter+1))
    else:
        shortest_path.append('')
del taken_nodes[str(target_node)]

for node in range(nodes_number - 1):

    # get the min node which is not selected yet
    min_node = min(taken_nodes, key=taken_nodes.get)
    min_node = int(min_node)

    # calculate the costs from it to the available nodes and replace it if smaller
    for path in range(nodes_number):
        if (nodes_paths[min_node][path] + shortest_cost[min_node] < shortest_cost[path]):
            shortest_cost[path] = nodes_paths[min_node][path] + shortest_cost[min_node]
            shortest_path[path] = shortest_path[min_node] + ' + from ' + str(min_node + 1) + 'to ' + str(path + 1)

    del taken_nodes[str(min_node)]

print(shortest_cost)
print(shortest_path)