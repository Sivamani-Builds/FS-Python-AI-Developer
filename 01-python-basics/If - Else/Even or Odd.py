# Write a python Program.If it is Even or Odd
value=input("Enter Any Value:")
if(value==value[::-1]):
    print("\t{} is Palindrome ".format(value))
elif (value != value[::-1]):
    print("\t{} is not Palindrome".format(value))