items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
  sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
  selected = {}
  total_cost = 0

  for name, data in sorted_items:
    if total_cost + data['cost'] <= budget:
      selected[name] = data
      total_cost += data['cost']

  return selected

def dynamic_programming(items, budget):
  names = list(items.keys())
  n = len(names)
  dp = [0] * (budget + 1)
  picks = [set() for _ in range(budget + 1)]

  for i in range(n):
    name = names[i]
    cost = items[name]['cost']
    calories = items[name]['calories']
    for b in range(budget, cost - 1, -1):
      if dp[b - cost] + calories > dp[b]:
        dp[b] = dp[b - cost] + calories
        picks[b] = picks[b - cost].copy()
        picks[b].add(name)

  best_set = picks[budget]
  return {name: items[name] for name in best_set}

budget = 100

print("Жадібний алгоритм:")
greedy = greedy_algorithm(items, budget)
for k, v in greedy.items():
    print(f"{k}: {v}")

print("\nДинамічне програмування:")
dp = dynamic_programming(items, budget)
for k, v in dp.items():
    print(f"{k}: {v}")