import random

list_size = 10

random_list = [random.randint(0,1000) for _ in range(list_size)]
ordered_list = sorted(random_list)

print(f"Lista desordenada: {random_list}")
print(f"\nLista ordenada: {ordered_list}")




