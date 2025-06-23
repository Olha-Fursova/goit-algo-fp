import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# Створюємо вузол дерева
class Node:
  def __init__(self, val, index):
    self.val = val
    self.index = index
    self.left = None
    self.right = None

# Побудова дерева з масиву
def build_tree(arr):
  def helper(i):
    if i >= len(arr):
      return None
    node = Node(arr[i], i)
    node.left = helper(2 * i + 1)
    node.right = helper(2 * i + 2)
    return node
  return helper(0)

# Побудова графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node:
    graph.add_node(node.index, label=node.val, color="#CCCCCC")
    if node.left:
      graph.add_edge(node.index, node.left.index)
      pos[node.left.index] = (x - 1 / 2 ** layer, y - 1)
      add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)
    if node.right:
      graph.add_edge(node.index, node.right.index)
      pos[node.right.index] = (x + 1 / 2 ** layer, y - 1)
      add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)

# Генерація кольору на основі позиції
def get_gradient_color(index, total):
  intensity = int(255 - (index / total) * 200)  # Від світлого до темного
  hex_color = f"#{intensity:02X}{intensity:02X}FF"
  return hex_color

# DFS 
def dfs_visualize(root):
  G = nx.DiGraph()
  pos = {root.index: (0, 0)}
  add_edges(G, root, pos)

  stack = [root]
  visited = set()
  order = []

  while stack:
    node = stack.pop()
    if node.index not in visited:
      visited.add(node.index)
      order.append(node.index)
      if node.right: stack.append(node.right)
      if node.left: stack.append(node.left)

  # Присвоюємо кольори
  for idx, node_index in enumerate(order):
    color = get_gradient_color(idx, len(order))
    G.nodes[node_index]['color'] = color

  # Малюємо граф
  colors = [G.nodes[n]['color'] for n in G.nodes]
  labels = {n: G.nodes[n]['label'] for n in G.nodes}

  plt.figure(figsize=(8, 5))
  nx.draw(G, pos=pos, labels=labels, node_color=colors, node_size=2500)
  plt.title("DFS обхід дерева")
  plt.show()

# BFS 
def bfs_visualize(root):
  G = nx.DiGraph()
  pos = {root.index: (0, 0)}
  add_edges(G, root, pos)

  queue = deque([root])
  visited = set()
  order = []

  while queue:
    node = queue.popleft()
    if node.index not in visited:
      visited.add(node.index)
      order.append(node.index)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  # Присвоєння кольору
  for idx, node_index in enumerate(order):
    G.nodes[node_index]['color'] = get_gradient_color(idx, len(order))

  # Побудова графіка
  colors = [G.nodes[n]['color'] for n in G.nodes]
  labels = {n: G.nodes[n]['label'] for n in G.nodes}

  plt.figure(figsize=(8, 5))
  nx.draw(G, pos=pos, labels=labels, node_color=colors, node_size=2500)
  plt.title("BFS обхід дерева")
  plt.show()

# tree_values = [1, 2, 3, 4, 5, 6, 7]
# root = build_tree(tree_values)
# dfs_visualize(root)

# tree_vals = [1, 2, 3, 4, 5, 6, 7]
# root = build_tree(tree_vals)
# bfs_visualize(root)