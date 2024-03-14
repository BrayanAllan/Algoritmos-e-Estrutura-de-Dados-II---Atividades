import random

def validate_ordering(ordered_list):

    for i in range (len(ordered_list)-1):
        
        if (ordered_list[i] <= ordered_list[i+1]):
            
            return True
        
        else:

            return False

list_size = 10

random_list = [random.randint(0,1000) for _ in range(list_size)]
ordered_list = sorted(random_list)

print(f"Lista desordenada: {random_list}")
print(f"\nLista ordenada: {ordered_list}")


if validate_ordering(ordered_list) == True:

    print("A lista está ordenada corretamente!")

else:

    print("A lista não está ordenada corretamente!")
