"""
非對稱式加解密
"""

import base64

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 產生一對 RSA 金鑰
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# 將私鑰序列化為 PEM 格式，以便保存到文件
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# PEM 轉回 Key
private_key2 = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
)

# 取得公鑰
public_key = private_key.public_key()

# 將公鑰序列化為 PEM 格式，以便保存到文件
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# PEM 轉回 Key
public_key2 = serialization.load_pem_public_key(
    public_key_pem,
)

# 待加密字串
message = "Hello World !"
print(message)

# 加密
cipherbytes = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 將加密結果從 bytes 轉為 str
ciphertext = base64.b64encode(cipherbytes).decode('utf-8')
print(ciphertext)
# 將加密結果從 str 轉回 bytes
cipherbytes = base64.b64decode(ciphertext.encode('utf-8'))

# 解密
plaintext = private_key.decrypt(
    cipherbytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 原文
print(plaintext.decode())
