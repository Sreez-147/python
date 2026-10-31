# string functions
# str1="py"
# print(str1)

# str1='If you trouble the trouble,trouble will troubles you. I am not trouble, I am the truth'
# print(str1)

str1='''If you trouble the trouble,trouble will troubles you. I am not the trouble, I am the truth ---by JAI Balayya@9999'''
# lower=str1.lower()
# print(lower)
# capitalize=str1.capitalize()
# print(capitalize)
# # print(str1.title())
# # upper=str1.upper()
# # print(upper)

# #  checking methods
# print(str1.islower())
# print(str1.isupper())
# print(str1.isalnum())
# print("sdsHIKsd14@37".isalnum())
# print("23456".isdigit())
# print(str1.count('trouble'))
print(str1)
# print(str1.rstrip())
# print(str1.lstrip())
# print(str1.strip())
words = str1.split()
print(words)
print(len(words))
print(type(words))
print(str1.count("the"))
# combined_string="".join(words)
# print(combined_string)
combined_string="@".join(words)
print(combined_string)