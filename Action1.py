#-------Action1：求2+4+6+8+...+100的求和------------
sum=0
for i in range(101):
    if i%2==0:
        sum=sum+i
print(sum)
