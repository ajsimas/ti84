def list_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

def main():
    try:
        number = int(input("Enter an integer to find its factors: "))
        factors = list_factors(number)
        print("Factors of", number, "are:", factors)
    except ValueError:
        print("Please enter a valid integer.")

main()
