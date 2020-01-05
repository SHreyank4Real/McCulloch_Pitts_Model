#XOR
x1=int(input("enter the value of x1"))
x2=int(input("enter the value of x2"))
zin1=x1-x2
if zin1 >=1:
    zin1=1
else:
    zin1=0
zin2=x2-x1
if zin2 >=1:
    zin2=1
else:
    zin2=0
yin=zin1+zin2
if yin >=1:
    yin=1
else:
    yin=0
print(yin)