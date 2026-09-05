# Write a python Program.If it is Even or Odd
n=float(input("Enter Any Numerical Value:"))
n=-15
res="EVEN" if (n>0) and (n%2==0) else "ODD" if(n>0) and (n%2!=0) else "Invalid Input "
print("{} is {}".format(n,res))