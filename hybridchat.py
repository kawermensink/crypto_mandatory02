import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, Box

# SHARED KEY
shared_key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
shared_box = nacl.secret.SecretBox(shared_key)
print('')
print("Orig key:", shared_key)

### SENDER ###

# keypair client 
skclient = PrivateKey.generate()
pkclient = skclient.public_key

# keypair chat
skchat = PrivateKey.generate()
pkchat = skchat.public_key

# create 'box' to send message
client_box = Box(skclient, pkchat)

# encrypt the shared_key
encrypted_shared_key = client_box.encrypt(shared_key)

### RECIEVER ###

chat_box = Box(skchat, pkclient)
received_shared_key = chat_box.decrypt(encrypted_shared_key)
reciever_box = nacl.secret.SecretBox(received_shared_key)

print("Send Key:", received_shared_key)
print('')

