import hashlib

md5hasher =hashlib .md5()
hash5=md5hasher.hexdigest()
print("MD5 hash is:",hash5)



md5hasher =hashlib .md5(b'alice')
hash5=md5hasher.hexdigest()
print("MD5 hash is:",hash5)
