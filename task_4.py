import uuid
import matplotlib.pyplot as plt
import networkx as nx

class HeapNode:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None
    self.id = str(uuid.uuid4())

# Побудова дерева з купи
def build_heap_tree(heap):
  def helper(index):
    if index >= len(heap):
      return None
    node = HeapNode(heap[index])
    node.left = helper(2 * index + 1)
    node.right = helper(2 * index + 2)
    return node

  return helper(0)

# Додаю вузли й зв'язки в граф
def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, label=node.val)
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

# Малюємо дерево
def draw_heap(root):
  G = nx.DiGraph()
  pos = {root.id: (0, 0)}
  add_edges(G, root, pos)

  labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}

  plt.figure(figsize=(8, 5))
  nx.draw(G, pos, labels=labels, arrows=False, node_size=2500, node_color='lightgreen')
  plt.title("Бінарна купа")
  plt.show()



# Тест
heap = [1, 3, 6, 5, 9, 8]
root = build_heap_tree(heap)
draw_heap(root)
