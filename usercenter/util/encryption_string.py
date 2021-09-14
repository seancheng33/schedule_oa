import hashlib

def md5_encrypt(passStr):
    hashstr = hashlib.md5()
    hashstr.update(passStr.encode(encoding='utf-8'))

    return hashstr.hexdigest()