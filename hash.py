import hashlib

print("SHA -1 has of word alice is:\n", hashlib.sha1(b'alice').hexdigest())
print("SHA-256 has of word alice is:\n", hashlib.sha256(b'alice').hexdigest())