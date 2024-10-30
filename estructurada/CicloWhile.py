if __name__ == '__main__':
    num = int (input("Proporciona un numero: "))
    fact = 1
    i = 1
    while i < num:
        fact = fact * i
        i = 1 + 1
        print(f"el factorial de {num} es: {fact}")