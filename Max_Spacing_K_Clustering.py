class Graph:
    def __init__(self, file_loc):
        lines = open(file_loc, 'r')
        num_nodes = int(lines.readline())
        G = []
        nodes = set()
        for line in lines:
            node1, node2, weight = map(int, line.split())
            edge = weight, (node1, node2)
            nodes.add(node1)
            nodes.add(node2)
            G.append(edge)
        G.sort()
        self.G = G
        self.num_nodes = num_nodes
        self.nodes= nodes

class Clusters:
    def __init__(self, Graph):
        self.G = Graph.G
        self.num_cluster = Graph.num_nodes
        self.nodes = Graph.nodes
        self.clusters = [{node} for node in Graph.nodes]

    def find(self, node):
        #find cluster that contain the node
        for i, cluster in enumerate(self.clusters):
            if node in cluster:
                #print('found ', node, ' in ','cluster ', i)
                return i
        print(node, ' not found') 

    def merge_clusters(self, node1, node2):
        #find cluster that contains node1
        cluster1 = self.find(node1)
        #find cluster that containfs node2
        cluster2 = self.find(node2)
        if cluster1 != cluster2:
            #merge two clusters
            #print('merging ', cluster1, ' and ',cluster2 )
            self.clusters[cluster1].update(self.clusters[cluster2])
            #reduce the num_cluter by 1
            self.clusters.pop(cluster2)
            self.num_cluster += -1

    def max_space_k_cluster(self, max_clusters):
        max_dist = float('-inf')
        for edge in self.G:
            if self.num_cluster < max_clusters:
                break
            else:
                dist, node1, node2 = edge[0], edge[1][0], edge[1][1]
                self.merge_clusters(node1, node2)
                if dist > max_dist:
                    max_dist = dist
        return max_dist

file_loc = 'clustering1.txt'
G = Graph(file_loc)
C = Clusters(G)
C.max_space_k_cluster(4)



        




