import nacl.utils
from nacl.public import PrivateKey, Box

### SENDER ###

# keypair client 
skclient = PrivateKey.generate()
pkclient = skclient.public_key

# keypair chat
skchat = PrivateKey.generate()
pkchat = skchat.public_key

# create 'box' to send message
client_box = Box(skclient, pkchat)

message = b"Axel, Ingvar og Kasper"

# encrypt message (with nonce)
encrypted = client_box.encrypt(message)
print(encrypted)

### RECIEVER ###

chat_box = Box(skchat, pkclient)

plaintext =chat_box.decrypt(encrypted)

print("Asym Message:", plaintext.decode('utf-8'))