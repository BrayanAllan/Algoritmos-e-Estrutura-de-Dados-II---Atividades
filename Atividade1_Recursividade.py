def factorial(number):

    if (number == 0):
        
        return  1
    
    else:

      return number * factorial (number-1)

number = 0

while(number != int):

    try:
        number = int(input("Informe o número que deseja calcular o fatorial: "))
        print(f"O fatorial de {number} é {(factorial(number))}.")
        break

    except:

        print("Informe um número!")
