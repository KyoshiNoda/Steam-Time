import bcrypt

def hash_string(string: str):
    """
    Returns a salted hash of the string using bcrypt
    """
    return bcrypt.hashpw(string.encode('utf8'), bcrypt.gensalt())

def compare_hash(hash_a: str, hash_b: str):
    """
    @param hash_a: Unhashed encoded string
    @param hash_b: Hashed encoded string\n
    Compare two hashes and returns the result.
    Both Hash Strings must be encoded with utf8
    """
    return bcrypt.checkpw(hash_a, hash_b)

