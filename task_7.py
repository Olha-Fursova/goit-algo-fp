import random
import matplotlib.pyplot as plt

#Симуляція методом Монте-Карло
def monte_carlo_dice_simulation(trials=100000):
  results = {i: 0 for i in range(2, 13)}

  for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    results[total] += 1

  # Перетворюємо в ймовірності
  probabilities = {k: v / trials for k, v in results.items()}
  return probabilities

# Аналітичні ймовірності
def analytical_probabilities():
  return {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
  }

# Побудова графіка порівняння
def plot_probabilities(simulated, theoretical):
  sums = list(range(2, 13))
  sim_vals = [simulated[s] for s in sums]
  theo_vals = [theoretical[s] for s in sums]

  x = range(len(sums))
  plt.bar(x, sim_vals, width=0.4, label='Монте-Карло', align='center')
  plt.bar([i + 0.4 for i in x], theo_vals, width=0.4, label='Аналітичні', align='center')

  plt.xticks([i + 0.2 for i in x], sums)
  plt.xlabel('Сума на кубиках')
  plt.ylabel('Ймовірність')
  plt.title('Ймовірність суми при киданні 2 кубиків')
  plt.legend()
  plt.grid()
  plt.show()

simulated = monte_carlo_dice_simulation(100000)
theoretical = analytical_probabilities()

plot_probabilities(simulated, theoretical)