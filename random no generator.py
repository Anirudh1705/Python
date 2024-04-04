import random

def generate_otp(num_digits=6):
    """Generate a random OTP with specified number of digits"""
    otp = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
    return otp

def generate_and_print_otp():
    """Generate a random 5-digit OTP and print it"""
    otp = generate_otp(6)
    print(f"Your OTP is: {otp}")

if __name__ == "__main__":
    generate_and_print_otp()