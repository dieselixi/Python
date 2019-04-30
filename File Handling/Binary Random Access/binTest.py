import os
import struct
filename = "rafile.dat"
recordSize = 28

fileSize = os.path.getsize(filename)
if fileSize % recordSize != 0:
    print("Error: Corrupted file")
else:
    numberRecords = fileSize // recordSize
    with open(filename, mode="rb") as file:
        for recordNumber in range(1, numberRecords + 1):
            fileContent = file.read(recordSize)
            tpl = struct.unpack(">3s5siiid", fileContent[:28])
            print("%3d: %s" % (recordNumber, str(tpl)))
