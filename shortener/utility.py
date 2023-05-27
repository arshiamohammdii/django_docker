from hashlib import md5
from base64 import b64encode

def hash_url(url):
    b = url.encode()
    return md5(b).hexdigest()[:8]



