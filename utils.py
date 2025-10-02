# utils.py
from cryptography.fernet import Fernet

# Generate a new key
def generate_key():
    return Fernet.generate_key()

# Save key to a file
def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the saved key
def load_key(filename="secret.key"):
    return open(filename, "rb").read()

# Encrypt data
def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data)

# Decrypt data
def decrypt_data(token, key):
    f = Fernet(key)
    return f.decrypt(token)
