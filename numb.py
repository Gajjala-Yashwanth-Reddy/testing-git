def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # Check for divisibility from 2 to square root of number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Example usage to find prime numbers in a range
def find_primes_up_to(n):
    prime_numbers = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Test the functions
if __name__ == "__main__":
    
    # Find all prime numbers up to 30
    primes = find_primes_up_to(30)
    print(f"Prime numbers up to 30: {primes}")
