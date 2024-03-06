from dh_starter_5_decrypt import decrypt_flag

g = 2
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

res = {
	"iv": "360fd616ccf878d9536070b49c4befff",
	"encrypted_flag": "860003a208821d39db27ce7b39ea87c85ed42ac073409b144fb9a143409f2361"
}

#res = {
#	"iv": "cc271adfa7affb9987282a4fc598fff9",
#    "encrypted_flag": "bc7f0042b405f80a3ce86e6c03c06bc1c2492249b21ab442ec20d0824c52d410"
#}

#res = {
#    'iv': '737561146ff8194f45290f5766ed6aba',
#    'encrypted_flag': '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'
#}


shared_secret = 0x01

flag = decrypt_flag(shared_secret, res['iv'], res['encrypted_flag'])
print(flag)