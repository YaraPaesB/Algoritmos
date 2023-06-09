def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq


x = int(input("Quantos elementos da sequencia de fibonacci você quer ver? "))
fib_seq = fibonacci(x)
print(fib_seq)