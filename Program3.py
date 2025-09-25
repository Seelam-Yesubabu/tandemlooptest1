a = int(input("Enter a number: "))

if a%2 == 0:
    terms=a-1   
else:
    terms=a       
for i in range(1,terms*2,2):
    print(i,end=" ")
