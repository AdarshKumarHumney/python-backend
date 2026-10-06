import hashlib
import secrets

plain_pass = "pass123"
salt = secrets.token_hex(16)
print(f"generated token - {salt}")

hash_byte = hashlib.pbkdf2_hmac("sha256",
                                plain_pass.encode("utf-8"),
                                salt.encode("utf-8"),
                                iterations=100_000,)
hash_hex = hash_byte.hex()
print(f"Derived hass - {hash_hex}")
stored_token = f"{salt}:{hash_hex}"
print(f"Database column :\n{stored_token}")