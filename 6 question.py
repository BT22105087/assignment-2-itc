len1=input(" length of first side")
len2=input(" length of second side")
len3=input(" length of third side")
len1=float(len1)
len2=float(len2)
len3=float(len3)
if len1+len2>len3 and len2+len3>len1 and len3+len1>len2:
    print("yes")
else:
    print("no")
