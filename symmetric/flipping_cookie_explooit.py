from requests import get
from Crypto.Util.Padding import pad
from pwn import xor


URL = 'https://aes.cryptohack.org/flipping_cookie/'
URL_GET_COOKIE = f'{URL}get_cookie/'
def URL_CHECK_ADMIN(cookie, iv):
	return f'{URL}check_admin/{cookie}/{iv}/'


iv_cookie = get(URL_GET_COOKIE).json()['cookie']
iv = bytes.fromhex(iv_cookie[:32])
cookie = bytes.fromhex(iv_cookie[32:])
print(f'iv     = {iv.hex()}')
print(f'cookie = {cookie.hex()}')

# use iv such that False becomes True
iv_forged = iv[:6] + xor(iv[6:11], b'False', b'True;') + iv[11:]
print(f'iv_f   = {iv_forged.hex()}')

dec = get(URL_CHECK_ADMIN(cookie.hex(), iv_forged.hex())).json()
print(f'dec    = {dec}')

flag = dec['flag']
print(f'flag   = {flag}')
