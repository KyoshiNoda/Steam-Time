import bcrypt

def hash_string(string):
    """
    Returns a salted hash of the string using bcrypt
    """
    return bcrypt.hashpw(string.encode('utf8'), bcrypt.gensalt())

def compare_hash(hash_a, hash_b):
    """
    @param hash_a: Unhashed encoded string
    @param hash_b: Hashed encoded string
    Compare two hashes and returns the result\n
    Both Hash Strings must be encoded with utf8
    """
    return bcrypt.checkpw(hash_a, hash_b)


def main():
    hash_1 = hash_string("abcdefg")
    hash_2 = u"abcdefg".encode('utf8')
    print(compare_hash(hash_2, hash_1))

if __name__ == "__main__":
    main()
