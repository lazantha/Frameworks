import hashlib
import os


# user_input="Lasantha"

# encode=hashlib.new('SHA256')
# encode.update(password.encode())
# hashed_password=encode.hexdigest()


# encode=hashlib.new('SHA256')
# encode.update(user_input.encode())
# new_hashed=encode.hexdigest()


# if hashed_password==new_hashed:
# 	print("maches")
# else:
# 	print("Did not mach")
# 	print(hashed_password)
# 	print(new_hashed)
# complete
# def hashPassword(password):

# 	encode=hashlib.new('SHA256')
# 	encode.update(password.encode())
# 	hashed_password=encode.hexdigest()
# 	return hashed_password

# password="lasantha"
# password_2="Lasantha"
# print(hashPassword(password)==hashPassword(password_2))


# password='lasantha'
# user_input='Lasantha'

# template=hashlib.new('SHA256')
# template.update(password.encode())
# hashed=template.hexdigest()
# print(hashed)

current_dir = os.getcwd()
print(current_dir)
