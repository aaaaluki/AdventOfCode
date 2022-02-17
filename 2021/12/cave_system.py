

class CaveSystem:

    def __init__(self, arr):

        cache = {}

        start_node = None
        end_node = None

        for pair in arr:
            tmp = pair.split('-')
            node_left = tmp[0]
            node_right = tmp[1]

            if node_left not in cache:
                cache[node_left] = Node(node_left)
                node_left = cache[node_left]

            else:
                node_left = cache[node_left]
            
            if node_right not in cache:
                cache[node_right] = Node(node_right)
                node_right = cache[node_right]

            else:
                node_right = cache[node_right]
            
            node_left.link(node_right)

            # Check for start and end nodes
            if node_left.isstart():
                start_node = node_left

            if node_right.isstart():
                start_node = node_right

            if node_left.isend():
                end_node = node_left

            if node_right.isend():
                end_node = node_right


        self.m_system = list(cache.values())

        # Remove caves only connected to a small cave
        while True:
            prev_len = len(self.m_system)
            for n in self.m_system:
                if n.isstart() or n.isend():
                    continue

                neigh = n.neighbours() 
                if len(neigh) == 1 and not neigh[0].isbig():
                    neigh[0].neighbours().remove(n)
                    self.m_system.remove(n)
                    print('Removed: {}'.format(n.dest()))
            
            if prev_len == len(self.m_system):
                break

        # Set the start and end nodes to the beginning and the end of the list
        # respectively
        self.m_system.remove(start_node)
        self.m_system.remove(end_node)
        self.m_system = [start_node] + self.m_system + [end_node]

        for n in self.m_system:
            print('Node {}:'.format(str(n)))

            for c in n.neighbours():
                print('\t{}'.format(str(c)))
    

    def find_paths(self, node=None, seen=None):
        if node.isend():
            return 1
        
        paths = 0
        for n in node.neighbours():
            if n.issmall():
                if n not in seen:
                    paths += self.find_paths(n, seen | {n})

            else:
                paths += self.find_paths(n, seen | {n})
        
        return paths

        

class Node:

    def __init__(self, dest:str):
        self.m_dest = dest
        self.m_neighbours = []
        self.m_start = False
        self.m_end = False
        self.m_big = False
        self.m_visited = False

        if self.m_dest == 'start':
            self.m_start = True

        elif self.m_dest == 'end':
            self.m_end = True
        
        else:
            self.m_big = self.m_dest.isupper()

    def link(self, node) -> None:
        self.m_neighbours.append(node)
        node.m_neighbours.append(self)

    def dest(self) -> str:
        return self.m_dest

    def neighbours(self) -> list:
        return self.m_neighbours

    def isstart(self) -> bool:
        return self.m_start

    def isend(self) -> bool:
        return self.m_end

    def isbig(self) -> bool:
        return self.m_big

    def issmall(self) -> bool:
        return not self.m_big

    def visit(self):
        self.m_visited = True
    
    def visited(self) -> bool:
        return self.m_visited

    def __str__(self) -> str:
        return self.m_dest