from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

key = rsa.generate_private_key(
    backend=crypto_default_backend(), public_exponent=65537, key_size=2048
)

private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption(),
)

public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH, crypto_serialization.PublicFormat.OpenSSH
)

with open("../public.pem", "wb") as file:
    file.write(public_key)

with open("../private.pem", "wb") as file:
    file.write(private_key)
