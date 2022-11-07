import csv

import warnings
warnings.filterwarnings('ignore')

class System:
    steps = [   
        [-1,0], # Top Step
        [0,1],  # Right Step
        [1,0], # Bottom Step
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city=list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows=len(self.star_city)
        self.star_city_cols=len(self.star_city[0])

    def check_limits(self,row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self,row,col):
        neighbours=[]
        #loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0],col+i[1]) not in neighbours:
                    neighbours.append((row+i[0],col+i[1]))
        return neighbours

    def find_route(self,source,destination):
        source = source
        destination = destination
        queue = [source]
        explored = []
        
        if source == destination:
            return "Same Node"
        
        while queue:
            path = queue.pop(0)
            if(len(explored) == 0):
                node = [path][-1]
            else:
                node = path[-1]
            if node not in explored:
                neighbours = self.get_neighbours(node[0], node[1])
                
                for neighbour in neighbours:
                    new_path = [path]
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == destination:
                        return new_path
                explored.append(node)
                
        return 

    def Bluevalley_to_Smallville_route(self, source, destination):
        route = self.find_route(source, destination)
        if(route == None):
            return "No Path Found!"
        else:
            return route 
        
if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    route = test_system1.find_route((3,0),(4,2))
    
    from collections import Iterable
    
    def flatten(lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in flatten(item):
                    yield x
            else:        
                yield item
    
    route = list(flatten(route))
    
    def list_create(x):
        l = []
        i = 0
        while (i < len(x)-1):
            l.append((x[i], x[i+1]))
            i = i+2
        return l

    route = list_create(route)
    
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for nodenum,node in enumerate(route):
        if nodenum != len(route)-1:
            print(f"({node[0]},{node[1]}) ---->", end=" ")
        else:
            print(f"({node[0]},{node[1]})", end=" ")
    
    #Finding path between Bluevalley to Smallville   
    start_city = (3, 0)
    destination_city = (3, 4)
    route = test_system1.Bluevalley_to_Smallville_route(start_city, destination_city)
    print('\n\nTo reach city Smallville from city Blue Valley the nodes traversed are-')
    if (route != 'No Path Found!'):
        route = list(flatten(route))
        route = list_create(route)
        for nodenum,node in enumerate(route):
            if nodenum != len(route)-1:
                print(f"({node[0]},{node[1]}) ---->", end=" ")
            else:
                print(f"({node[0]},{node[1]})", end=" ")
    else:
        print(route)