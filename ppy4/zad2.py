def prime(*number):
    for num in number:
        if num == 0 or num == 1:
            print(num, "is not prime")
        elif num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not prime")
                    break
            else:
                print(num, "is prime number")


prime(0, 1, 2, 3, 4, 5)
