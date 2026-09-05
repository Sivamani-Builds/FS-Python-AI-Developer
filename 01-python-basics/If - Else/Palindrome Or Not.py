# Write a python Program, which will accept any Value whether It is Palindrome or Not
value=input("Enter Any Value:")
res= "Palindrome" if  value.upper()==value[::-1].upper() else "Not Palindrome"
print("{} is {}".format(value,res))