# binaryFile.py
# Colin kee
# 2018-11-04


import struct

def getInt(prompt, min, max):
    valid = False
    while not valid:
        try:
            n = int(input(prompt))
            while n < min or n > max:
                n = int(input("Integer value must be between {0} and {1}, please re-enter: ".format(min,max)))
            valid = True
        except ValueError:
            print("Error: Invalid Entry")
    return n

def getFloat(prompt, min, max):
    valid = False
    while not valid:
        try:
            n = float(input(prompt))
            while n < min or n > max:
                n = float(input("Double value must be between {0} and {1}, please re-enter: ".format(min,max)))
            valid = True
        except ValueError:
            print("Error: Invalid Entry")
    return n

def getChar(prompt, allowed):
    valid = False
    while not valid:
        ch = input(prompt)
        if len(ch) == 1 and ch in allowed:
            valid = True
        else:
            print("Error: Character entered is not a valid response.")
    return ch

fileName = "rafile.dat"
cont = "Y"
fileOut = open(fileName, "ab")
while cont == "Y":
    dept  = input("Enter dept ID: ").upper().rjust(3,' ').encode('utf-8')
    empID = input("Employee ID: ").upper().encode("utf-8")
    day = getInt("Enter day: ", 1, 31)
    month = getInt("Enter month: ", 1, 12)
    year = getInt("Enter year: ", 2000, 2100)
    hours = getFloat("Enter hours: ", 0.0, 24.0)
    record = struct.pack(">3s5siiid",dept, empID, day, month, year, hours)
    fileOut.write(record)
    cont = getChar("Enter another record (Y/N) ", "YyNn").upper()
fileOut.close()
print()
print("\nFile {0} has been modified.\n".format(fileName))
