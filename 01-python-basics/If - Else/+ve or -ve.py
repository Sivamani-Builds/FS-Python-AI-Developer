# Write a python Program.If it is  +VE Or -VE or ZERO
val=float(input("Enter Any Numerical Value:"))#10
if(val>0):
    print("\t{} is +VE".format(val))
elif(val<0):
    print("\t{} is -VE".format(val))
else:
    print("\t{} is ZERO".format(val))
print("I am from Outer-if-else Statement ")