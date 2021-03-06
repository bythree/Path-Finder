
# coding: utf-8

# In[15]:

import heapq
import pandas as pd


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def graph():

    nodes = pd.read_csv(r'..\Python scripts\DOPEROAD_DOPENODE.csv')
    roads = pd.read_csv(r'..\Python scripts\DOPEROAD_DOPENODE.csv')

    a = list(roads.IN)
    b = list(roads.OUT)
    distance = list(roads.DISTANCE)

    #print(a)

    #print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    #print(b)

    #print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    #print(distance)

    box=[]

    for i,j in enumerate(a):


        box.append([j,b[i],distance[i]])

    case = {i:[] for i in a}

    for i,v in enumerate(box):

        if v[0]==a[i]:

            case[a[i]].append(v[1:])

    return(case)


s = graph()

#print(s)
#h = (s[171])
#print(h)


# In[18]:


def dijkstra_search(graph,start, goal):
    
    #print(graph[173])
    
    graph = s
    
    INF = ((1<<63) - 1)//2
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = { x:x for x in graph } 
    #print(came_from)
    cost_so_far = { x: INF for x in graph }
    #print(cost_so_far)
    #cost_so_far = {}
    cost_so_far[start] = 0
    cost_so_far[goal] = INF
    mileage = 0
    
    while not frontier.empty():
        
        if start not in graph.keys():
            
            #print('There is no path from %s, to %s' % (start,goal))
            break
        
        #print(frontier.elements)
        current_node = frontier.get()
        #print('Current Node:',current_node)
        
    
        mileage += cost_so_far[current_node]

        #print("Mileage:",mileage)

        
        if current_node == goal or cost_so_far[goal]<mileage:
            #print('GOAL CAME FROM: ',came_from[goal],', Goal Cost: ',cost_so_far[goal],', Dijkstra Mileage: ',mileage, sep= '')
            #print('CURRENT NODDEEEEEEEEEE:',current_node)
            break
        
        for next_node in graph[current_node]:
            try:
                #print('GCN:',graph[current_node])
                #print('Next node:',next_node)
                n_id = next_node[0]
                #if n_id not in graph.keys():
                    #print(not in)
                #print('CURRENT COST:',cost_so_far[current_node])
                #print('NEXT NODE COST:',cost_so_far[n_id])
                #print('node id: ', n_id)
                n_dist = next_node[1]

                new_cost = cost_so_far[current_node] + n_dist

                #if n_id not in cost_so_far or 
                if new_cost < cost_so_far[n_id]:

                    #print('new cost: ',new_cost)
                    cost_so_far[n_id] = new_cost
                    #print('cost so far',cost_so_far[n_id])
                    priority = new_cost
                    frontier.put(n_id, priority)
                    came_from[n_id] = current_node
                    
                if n_id == goal:
                    
                    goal_miles = mileage
                    #print('GOAL MILEAGE:', goal_miles)
                    
            except:   
                     if (n_id == goal and n_id not in graph.keys()):
                        #print('GOAL CAME FROM',came_from[current_node],mileage)
                        #print('CURRENT NODDEEEEEEEEEE:',current_node)
                        break

                     pass
    

    if cost_so_far[goal] == INF:

        #print(('There is no path from %s, to %s') % (start,goal))
        return 0
        

    else:
        return came_from
        
    #if dist[target]==INF:
     #   stdout.write("There is no path between " + source + " and " + target)
    #print(cost_so_far)
    #, cost_so_far
    

    
j = dijkstra_search(s,356,924)



# In[20]:

def reconstruct_path(came_from, start, goal):
    
    if came_from == 0:
        return 0
    current_node = goal
    path = [current_node]
    while current_node != start:
        current_node = came_from[current_node]
        path.append(current_node)
    #path.append(start) # optional
    path.reverse() # optional
    #print([goal])
    return path

print(reconstruct_path(j, 356, 924))

