from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def fetch_public_key(user):
    with open(user.decode('ascii') + "key.pub", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
           key_file.read(),
           backend=default_backend())
    return public_key

# Message coming from user
message = b"Nelson likes cat"

# Signature coming from user
signature = b'\t\xf2!\x84Y\xcb\xd9\xd1b\xa3\xe3E\xbe\x90\xc2\xcef\x0f&1\xcf\xda\xb7\x8c\xc3\x80K\xeff8c\xe1\x10^\x97ew\x1eU\xf6\xa0\xc1^(dVX\xcc\xedI\xb2\x05\x93G\xb6\xdeH\x9c\xfb\xdf\xa2{z\xfc}\x9c\xd1\x8d\xb7\xbf\xc6`\x8c\xe2\r\x1f\x1f\xae\x04{)\x08i\xe3\xbc\xbeQv\xbfIJ\x97QM\x11K\xdcE*oC\x1fIc\x93\xa2\xd2\xbdT3^\x11\xad?\x964\x8d\xa9d\xaf\x9diz\xef3\x14|\xc1'

user = message.split()[0].lower()
# fetch public key from Nelson
public_key = fetch_public_key(user)
# … verify the message like before
public_key.verify(
    signature,
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256())
