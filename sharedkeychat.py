import nacl.secret
import nacl.utils

### SENDER ###

# shared key generator
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# used to encrypt/decrypt
box = nacl.secret.SecretBox(key)

message = b"Dette skal bruges til en cryptochat"

encrypted = box.encrypt(message)
print(encrypted)

### REVIEVER ###

plaintext = box.decrypt(encrypted)
print(plaintext.decode('utf-8'))