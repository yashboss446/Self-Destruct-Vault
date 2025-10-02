from utils import generate_key, save_key, load_key, encrypt_data, decrypt_data

# Step 1: Generate and save key (do this once)
key = generate_key()
save_key(key)

# Step 2: Load the key back
key = load_key()

# Step 3: Encrypt a message
message = b"My first secret data"
encrypted = encrypt_data(message, key)
print("🔒 Encrypted:", encrypted)

# Step 4: Decrypt the message
decrypted = decrypt_data(encrypted, key)
print("🔓 Decrypted:", decrypted.decode())
