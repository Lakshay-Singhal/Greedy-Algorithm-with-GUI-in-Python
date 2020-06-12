########################################the print widget###############################################################################
def print_widget(shortest_cost,shortest_path,target_node):
    print_widget = Tk()
    for counter in range(len(shortest_cost)):
        if(counter !=target_node):
            Label(print_widget,
                  text='the shortest cost from  (' + str(target_node + 1) + ') to (' + str(counter + 1) + ') is { ' + str(
                      shortest_cost[counter]) + ' }  ' + shortest_path[counter], borderwidth=1).grid(row=counter, column=0)

    print_widget.mainloop()

######################################## Implemting the algorithm #####################################################################
def algorithm(nodes_number,nodes_paths,target_node):
    shortest_cost = nodes_paths[target_node]
    shortest_path = []

    #make dictionary of all costs with key of node number
    taken_nodes = dict()
    for counter in range(nodes_number):
        taken_nodes[str(counter)] = shortest_cost[counter]

    # the first step for the target node
    for counter in range(len(shortest_cost)):
        if (shortest_cost[counter] != 999):
            shortest_path.append('from ' + str(target_node + 1) + 'to ---> ' + str(counter + 1))
        else:
            shortest_path.append('')
    del taken_nodes[str(target_node)]

    #the other steps for each node
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

    print_widget(shortest_cost,shortest_path,target_node)
################################################get the target node###################################################################
def get_target_node(Lb1,target_widget,nodes_number,nodes_paths):
    target_node=Lb1.get(Lb1.curselection())
    target_node=int(target_node)-1
    target_widget.destroy()
    algorithm(nodes_number,nodes_paths,target_node)
#############################################the target widget#########################################################################
def target_widget(nodes_number,nodes_paths):
    target_widget = Tk()
    Label(target_widget, text='Select the target node', borderwidth=1).grid(row=0, column=0)

    Lb1 = Listbox(target_widget)
    for counter in range(nodes_number):
        Lb1.insert(counter, str(counter+1))


    Lb1.grid(row=0, column=1)
    cmd2 = lambda: get_target_node(Lb1, target_widget,nodes_number,nodes_paths)
    B = Button(target_widget, text="Submit", command=cmd2)
    B.grid(row=1, column=0)
    target_widget.mainloop()
#############################make a list of costs from each node to the other###########################################################
def get_costs(entries_list,costs_widget,nodes_number):
    nodes_paths=[]
    for node in range(nodes_number):
        nodes_path=[]
        for counter in range(nodes_number):
            if(node==counter):
                nodes_path.append(0)
            else:
                nodes_path.append(int(entries_list[0].get()))
                del entries_list[0]
        nodes_paths.append(nodes_path)
    costs_widget.destroy()
    target_widget(nodes_number,nodes_paths)
############################### the widget of taking the costs and the target node ####################################################
def costs_widget(nodes_number):
    entries_list=[]
    costs_widget = Tk()
    for node in range(nodes_number):
        for counter in range(nodes_number):
            if  (node!=counter):
                Label(costs_widget, text='Enter the cost from node '+str(node+1)+' to node  '+str(counter+1), borderwidth=1).grid(row=(node*nodes_number)+counter, column=0)
                E1 = Entry(costs_widget, bd=5)
                E1.grid(row=(node*nodes_number)+counter, column=1)
                entries_list.append(E1)
    cmd1 = lambda: get_costs(entries_list,costs_widget,nodes_number)
    B = Button(costs_widget, text="Submit", command=cmd1)
    B.grid(row=nodes_number*nodes_number,column=0)
    costs_widget.mainloop()
################################################################get the number of the nodes ###########################################
def number_nodes(E1,number_widget):
    nodes_number = int(E1.get())
    number_widget.destroy()
    costs_widget(nodes_number)
##################################the widget of taking the Nodes Number################################################################
def number_widget():
    number_widget = Tk()
    Label(number_widget, text='Enter the number of the nodes', borderwidth=1).grid(row=0, column=0)
    E1 = Entry(number_widget, bd=5)
    E1.grid(row=0, column=1)
    cmd = lambda: number_nodes(E1,number_widget)
    B = Button(number_widget, text="Submit", command=cmd)
    B.grid(row=1,column=0)
    number_widget.mainloop()
############################# importing Tkinter and Intialize Variables ###############################################################
from tkinter import *
number_widget()
#######################################################################################################################################