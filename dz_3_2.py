def factorize(*number):
    i = 1
    numbers = []
    for n in number:
        while i <=n:
            if n % i == 0:
                numbers.append(i)
            i+=1
    print(numbers)

        # raise NotImplementedError() # Remove after implementation

factorize(1000000000)