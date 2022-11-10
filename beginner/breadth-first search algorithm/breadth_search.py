class Queue():
    def __init__(self):
        self.size = 0
        self.list = []
    def enqueue(self, data):
        self.list.append(data)
        self.size += 1
    def dequeue(self):
        try:
            self.size -= 1
            return self.list.pop(0)
        except Exception as error:
            print(f'{error} is not possible')
    def xprint(self, index):
        print(self.list[index])

# Now let’s see how to implement the Breadth-first algorithm using Python.
def breadth_first(graph, root):
    queue = Queue()
    visited_nodes = list()
    queue.enqueue(root)
    visited_nodes.append(root)
    current_node = root
    while queue.size > 0:
        current_node = queue.dequeue()
        adj_nodes = graph[current_node]
        remaining_elements = sorted(set(adj_nodes) - set(visited_nodes))
        if len(remaining_elements) > 0:
            for element in remaining_elements:
                visited_nodes.append(element)
                queue.enqueue(element)
    return visited_nodes

# Now let's create the dictionary of the chart to print the results of the breadth_first function passing the graph and the root.
if __name__ == '__main__':
    graph = dict()

    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']

    print(breadth_first(graph, 'A'))