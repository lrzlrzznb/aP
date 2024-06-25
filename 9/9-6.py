import sys
class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_ertex = Vertex(key)
        self.vertices[key] = new_ertex
        return new_ertex
    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
    def __len__(self):
        return self.num_vertices
    def __contains__(self, n):
        return n in self.vertices
    def add_edge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.add_vertex(f)
        if t not in self.vertices:
            nv = self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], cost)
    def getVertices(self):
        return list(self.vertices.keys())
    def __iter__(self):
        return iter(self.vertices.values())
class Vertex:
    def __init__(self, num):
        self.key = num
        self.connectedTo = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.previous = None
        self.disc = 0
        self.fin = 0
    def __lt__(self,o):
        return self.key < o.key
    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def get_neighbors(self):
        return self.connectedTo.keys()
    def __str__(self):
        return str(self.key) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.distance) + ":pred \n\t[" + str(self.previous) + "]\n"
def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):           
        for col in range(board_size):       
            node_id = pos_to_node_id(row, col, board_size) 
            new_positions = gen_legal_moves(row, col, board_size) 
            for row2, col2 in new_positions:
                other_node_id = pos_to_node_id(row2, col2, board_size)
                kt_graph.add_edge(node_id, other_node_id)
    return kt_graph

def pos_to_node_id(x, y, bdSize):
    return x * bdSize + y

def gen_legal_moves(row, col, board_size):
    new_moves = []
    move_offsets = [                  
        (-1, -2),  
        (-1, 2),  
        (-2, -1),  
        (-2, 1),  
        (1, -2),  
        (1, 2), 
        (2, -1),  
        (2, 1),  
    ]
    for r_off, c_off in move_offsets:
        if (                               
            0 <= row + r_off < board_size
            and 0 <= col + c_off < board_size
        ):
            new_moves.append((row + r_off, col + c_off))
    return new_moves
def knight_tour(n, path, u, limit):
    u.color = "gray"
    path.append(u)              
    if n < limit:
        neighbors = ordered_by_avail(u) 
        i = 0
        for nbr in neighbors:
            if nbr.color == "white" and \
                knight_tour(n + 1, path, nbr, limit):  
                return True
        else:                       
            path.pop()              
            u.color = "white"       
            return False
    else:
        return True
def ordered_by_avail(n):
    res_list = []
    for v in n.get_neighbors():
        if v.color == "white":
            c = 0
            for w in v.get_neighbors():
                if w.color == "white":
                    c += 1
            res_list.append((c,v))
    res_list.sort(key = lambda x: x[0])
    return [y[1] for y in res_list]
def main():
    def NodeToPos(id):
       return ((id//8, id%8))
    bdSize = int(input()) 
    *start_pos, = map(int, input().split())
    g = knight_graph(bdSize)
    start_vertex = g.get_vertex(pos_to_node_id(start_pos[0], start_pos[1], bdSize))
    if start_vertex is None:
        print("fail")
        exit(0)
    tour_path = []
    done = knight_tour(0, tour_path, start_vertex, bdSize * bdSize-1)
    if done:
        print("success")
    else:
        print("fail")
    exit(0)
if __name__ == '__main__':
    main()