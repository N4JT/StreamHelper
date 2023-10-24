import os

def generateKey():
    key = os.urandom(32)

# Convert the binary key to a hexadecimal string
    hex_key = key.hex()

    print("Generated 256-bit key (32 bytes):")
    print(hex_key)
    return hex_key
