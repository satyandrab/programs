def main(number):
    fact = 1
    if number <= 1:
        return 1
    else:
        for i in range(1, number+1):
            fact = fact * i
        return fact
if __name__ == "__main__":
    n = int(raw_input("Please enter number for factorial...."))
    factorial = main(n)
    print factorial