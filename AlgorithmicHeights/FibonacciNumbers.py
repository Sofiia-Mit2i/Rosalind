def Fibonacci (n):
    if n <= 25:
       numbers = [0,1]
       while len(numbers) <= n:
             i = numbers[-2] + numbers[-1]
             numbers.append(i)
       result = numbers[-1]
       print(f'Your Fibonacci Number is: {result}')
    else:
        print("Your number has to be less than 25. ")

n = int(input("Enter your number: "))
Fibonacci(n)

