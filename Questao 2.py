def sequencia_fibonacc(num):
    if num < 0:
        return False, []
    
    fibonacci = [0, 1]
    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    pertence = num in fibonacci
    return pertence, fibonacci

numero = int(input("Informe um número: "))
pertence, sequencia = sequencia_fibonacc(numero)

if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

print(f"Sequência de Fibonacci até o número informado: {sequencia}")