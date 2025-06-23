import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth, ax):
  if depth == 0:
    return
  
  x_end = x + length * np.cos(angle)
  y_end = y + length * np.sin(angle)
  
  # Створення лінії (гілки)
  ax.plot([x, x_end], [y, y_end], color=plt.cm.viridis(depth / 10))

  # Рекурсивний виклик для двох гілок
  new_length = length * 0.7
  draw_tree(x_end, y_end, angle + np.pi / 4, new_length, depth - 1, ax)
  draw_tree(x_end, y_end, angle - np.pi / 4, new_length, depth - 1, ax)

def main():
  depth = int(input("Введіть рівень рекурсії (наприклад, 6): \n>> "))

  fig, ax = plt.subplots()
  ax.set_aspect("equal")
  ax.axis("off")
  
  # Визначення основних параметрів
  draw_tree(0, 0, np.pi / 2, 100, depth, ax)

  plt.show()

main()