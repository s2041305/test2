from math import sqrt
for j in range(0,9):
    for i in range(0,9):
            for j2 in range(0,9):
                for i2 in range(0,9):
                    if ((i2==i) & (j2==j)):
                        continue
                    distance=sqrt((i2-i)**2+(j2-j)**2)
                    print(i,j,"to",i2,j2,"distance",distance)
