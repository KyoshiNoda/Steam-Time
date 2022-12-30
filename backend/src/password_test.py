import bcrypt

password = u"wowzer123"
hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

string_password = hashed_password.decode('utf8')

password = u"wowzer123"
print(bcrypt.checkpw(password.encode('utf8'), string_password.encode('utf8')))