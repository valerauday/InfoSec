import random
import time
from hashlib import sha3_256  # Changed from sha256 to sha3_256

def generate_keypair(p, q, g):
    """Generate public and private keys."""
    # This function remains unchanged
    x = random.randint(1, q - 1)  # Private key: random number
    y = pow(g, x, p)  # Public key: g^x mod p
    return (p, q, g, y), x

def sign(private_key, message):
    """Sign a message using the private key."""
    p, q, g, x = private_key
    k = random.randint(1, q - 1)  # Random nonce
    r = pow(g, k, p) % q  # First part of signature
    
    timestamp = int(time.time())  # Get current timestamp
    hash_message = int(sha3_256((message + str(timestamp)).encode()).hexdigest(), 16)  # Hash the message with timestamp
    s = (pow(k, -1, q) * (hash_message + x * r)) % q  # Second part of signature
    
    return (r, s, timestamp)  # Include timestamp in the signature

def verify(public_key, message, signature):
    """Verify the signature using the public key."""
    p, q, g, y = public_key
    r, s, timestamp = signature  # Unpack the timestamp from the signature
    
    if r <= 0 or r >= q or s <= 0 or s >= q:
        return False  # Invalid signature range
    
    hash_message = int(sha3_256((message + str(timestamp)).encode()).hexdigest(), 16)  # Hash the message with timestamp
    w = pow(s, -1, q)  # Modular inverse of s
    u1 = (hash_message * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q  # Verification calculation
    
    return v == r  # Signature is valid if v equals r

# Example usage
if __name__ == "__main__":
    # System parameters (small values for demonstration)
    p = 23  # Prime modulus
    q = 11  # Prime factor of p-1
    g = 4   # Generator

    # Generate keys
    public_key, private_key = generate_keypair(p, q, g)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Sign and verify a message
    message = "Hello, TimestampedDSA!"
    signature = sign((p, q, g, private_key), message)
    print("Signature:", signature)

    is_valid = verify(public_key, message, signature)
    print("Signature is valid:", is_valid)

    # Verify with a tampered message
    tampered_message = "Hello, TimestampedDSA tampered!"
    is_valid_tampered = verify(public_key, tampered_message, signature)
    print("Tampered signature is valid:", is_valid_tampered)

    # Demonstrate timestamp effect (wait for 1 second)
    time.sleep(3)
    is_valid_delayed = verify(public_key, message, signature)
    print("Delayed verification is valid:", is_valid_delayed)
