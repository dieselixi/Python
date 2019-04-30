# arrayCounter.py
# Colin kee
# 2018-10-23


print("This program counts digit frequencies in the input\n")

str1 = input("Enter a string (QUIT to exit): ")

ar = [0]*10

while str1.upper() != "QUIT":
    for i in range(0,len(str1),1):
        for j in range(0, len(ar), 1):
            if str1[i] == str(j):
                ar[j] +=1
    str1 = input("Enter another string (QUIT to exit): ")
for x in range(0,len(ar), 1):
    print("The count for digit {0} is {1}".format(x, ar[x]) )
