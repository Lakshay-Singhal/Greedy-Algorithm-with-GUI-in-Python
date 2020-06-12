selected = []
start = []
finish = []

def ActivitySelection(start, finish, n=len(start)):
    global selected
    selected=[]
    j = 0
    selected.append(j)
    for i in range(1,n):
        if start[i] >= finish[j]:
            selected.append(i)
            j = i