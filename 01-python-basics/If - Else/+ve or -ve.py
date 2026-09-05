# Write a python Program.If it is  +VE Or -VE or ZERO
n=float(input("Enter Any Numerical Value:"))
res="+VE"  if n>0 else "-VE" if n<0 else "ZERO"
print("{} is {}".format(n,res))
