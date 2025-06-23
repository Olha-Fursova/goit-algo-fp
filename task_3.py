import heapq

def dijkstra(graph, start):
  distances = {node: float("inf") for node in graph}
  distances[start] = 0
  
  # Черга з пріоритетом (відстань, вузол)
  heap = [(0, start)]

  while heap:
    current_distance, current_node = heapq.heappop(heap)
    
    # Пропускаємо, якщо знайшли коротший шлях раніше
    if current_distance > distances[current_node]:
      continue

    # Оновлення відстаней до сусідів
    for neighbor, weight  in graph[current_node].items():
      distance = current_distance + weight

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(heap, (distance, neighbor))

    return distances
  

# Тест
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

for node, dist in shortest_paths.items():
    print(f"Найкоротша відстань від {start_node} до {node}: {dist}")