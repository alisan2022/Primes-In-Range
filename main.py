low = int(input("Enter lower limit: "))
up = int(input("Enter upper limit: "))


def primes_between_range(lower,upper):
    prime_list = []

    print("Prime numbers between", lower, "and", upper, "are:")
    print("-------", end=" ")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")
                prime_list.append(num)


primes_between_range(low,up)