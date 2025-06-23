# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

# Починаю зі створення класу Node для елементів списку

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
# Додаю клас LinkedList для створення однозв'язного списку

class LinkedList:
  def __init__(self):
    self.head = None
  
  # Метод append для додавання нових елементів
  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      return
    
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node
  
  # Метод print_list() для виведення елементів списку

  def print_list(self):
    current = self.head
    while current:
      print(current.value, end=" ")
      current = current.next

  # Методи reverse() для обернення списку
  def reverse(self):
    prev = None
    current = self.head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev
  
  def get_middle(self, head):
    if head is None:
      return head
    
    # Створюю по дві змінні, які рухатимуться на один та два вузли вперед кожну ітерацію
    slow = head
    fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next
    return slow
  
  # Основна функція сортування
  def merge_sort(self, head):
    if head is None or head.next is None:
      return head
    
    # Знаходимо середину списку
    middle = self.get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивно сортуємо ліву і праву частину
    left = self.merge_sort(head)
    right = self.merge_sort(next_to_middle)

    # Об'єднуємо відсортовані частини
    sorted_list = self.sorted_merge(left, right)

    return sorted_list
  
  # Функція сортування та об'єднання двох відсортованих списків
  def sorted_merge(self, list_1, list_2):
    if not list_1:
      return list_2
    if not list_2:
      return list_1
    
    if list_1.value <= list_2.value:
      result = list_1
      result.next = self.sorted_merge(list_1.next, list_2)
    else:
      result = list_2
      result.next = self.sorted_merge(list_1, list_2.next)
    return result
  
  def sort(self):
    self.head = self.merge_sort(self.head)



# Тестування усіх функцій однозв'язного списку
ll1 = LinkedList()
ll2 = LinkedList()

for val in [5, 1, 6, 2, 8]:
  ll1.append(val)

for val in [4, 7, 3]:
  ll2.append(val)

print("Початковий список ll1:")
ll1.print_list()

print("\nПочатковий список ll2:")
ll2.print_list()

ll1.sort()
ll2.sort()

print("\nВідсортований список ll1:")
ll1.print_list()

print("\nВідсортований список ll2:")
ll2.print_list()

merged_list = LinkedList()
merged_list.head = merged_list.sorted_merge(ll1.head, ll2.head)

print("\nОб'єднаний відсортований список:")
merged_list.print_list()

merged_list.reverse()
print("\nРеверсований об'єднаний список:")
merged_list.print_list()