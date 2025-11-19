import random
import string

def generate_random_id(n=8):
    """Generate a random string of length n (default 8)."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))

# Example:
print(generate_random_id())  # e.g. 'a9Zk13Qp'