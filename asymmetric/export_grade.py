from dh_starter_5_decrypt import decrypt_flag
from sage.all import *

"""
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported": ["DH64"]}
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x2e01814127d50e2a"}
Intercepted from Bob: {"B": "0xae01353db86d6b1d"}
Intercepted from Alice: {"iv": "63acf5ed63379d97a97ceeaf0e507831", "encrypted_flag": "a09c6511975291c2c87c65503da5cb4555be2491be1086efe16ee3b41d0ff717"}
"""

p = 0xde26ab651b92a129
g = 2
A = 0x2e01814127d50e2a
B = 0xae01353db86d6b1d
g = mod(2,p)

iv = '63acf5ed63379d97a97ceeaf0e507831'
encrypted_flag = 'a09c6511975291c2c87c65503da5cb4555be2491be1086efe16ee3b41d0ff717'

a = discrete_log(A,g)

shared_secret = pow(B, a, p)

flag = decrypt_flag(shared_secret, iv, encrypted_flag)
print(flag)