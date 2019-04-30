# ControlBreakReport2.py
# Colin kee
# 2018-11-04


import struct

infile = open("cb2data.dat", "rb")
outfile = open("cb2rpt.txt", "w")

outfile.write("Daily hours worked by Department by Employee\n\n")
outfile.write("Dept EmpID     Date     Hours\n\n")

totHours = 0
empHours = 0
deptHours = 0

prevID = "$$$"
prevDept = "$$$"
recNum = 0

packedData = infile.read(3 + 5 + 4 + 4 + 4 + 8 )

while len(packedData) > 0:
    recNum += 1
    fields = struct.unpack(">3s5siiid", packedData)
    dept = fields[0].decode('utf-8')
    empID = fields[1].decode('utf-8')
    month = fields[2]
    day = fields[3]
    year= fields[4]
    hours = fields[5]
    if dept != prevDept and recNum > 1:
        # employee level break
        outfile.write("Employee total          {0:5.2f}\n\n".format(empHours))
        deptHours += empHours
        empHours = 0
        # department level break
        outfile.write("Department total       {0:6.2f}\n\n".format(deptHours))
        totHours += deptHours
        deptHours= 0
    elif empID != prevID and recNum > 1:
        # employee level break
        outfile.write("Employee total          {0:5.2f}\n\n".format(empHours))
        deptHours += empHours
        empHours = 0

    outfile.write("{0:>3s}  {1:5s}  {2:2d}/{3:02d}/{4:4d}  {5:5.2f}\n".format(dept, empID,month, day,year,hours))
    empHours += hours
    prevID = empID
    prevDept = dept
    packedData = infile.read(3 + 5 + 4 + 4 + 4 + 8 )

infile.close()

outfile.write("Employee total          {0:5.2f}\n\n".format(empHours))
deptHours += empHours
totHours += deptHours
# department level break
outfile.write("Department total       {0:6.2f}\n\n".format(deptHours))
outfile.write("Total hours worked     {0:6.2f}\n\n".format(totHours))
outfile.write("{0:>3d} records processed".format(recNum))

outfile.close()
