# ControlBreakReport1.py
# Colin kee
# CIS-111
# 2018-10-25

# This assignment involves the creation of a level break report by correctly implementing the supplied algorithm in Python.


infile = open("cb1data.txt")
outfile = open("report.txt", "w")

outfile.write("Daily hours worked by Department by Employee\n\n")
outfile.write("Dept EmpID     Date     Hours\n\n")

totHours = 0
empHours = 0
deptHours = 0

prevID = "$$$"
prevDept = "$$$"

recno = 0

for rec in infile:
    recno = recno + 1
    lst = rec.split(',')
    dept = lst[0].strip('"')
    empID = lst[1].strip('"')
    month = int(lst[2])
    day = int(lst[3])
    year= int(lst[4])
    hours = float(lst[5])
    if dept != prevDept and recno > 1:
        # employee level break
        outfile.write("Employee total          {0:5.2f}\n\n".format(empHours))
        deptHours += empHours
        empHours = 0
        # department level break
        outfile.write("Department total       {0:6.2f}\n\n".format(deptHours))
        totHours += deptHours
        deptHours= 0
    elif empID != prevID and recno > 1:
        # employee level break
        outfile.write("Employee total          {0:5.2f}\n\n".format(empHours))
        deptHours += empHours
        empHours = 0

    outfile.write("{0:>3s}  {1:5s}  {2:2d}/{3:02d}/{4:4d}  {5:5.2f}\n".format(dept, empID,month, day,year,hours))
    empHours += hours
    prevID = empID
    prevDept = dept

infile.close()

outfile.write("Employee total          {0:5.2f}\n\n".format(empHours))
deptHours += empHours
totHours += deptHours
# department level break
outfile.write("Department total       {0:6.2f}\n\n".format(deptHours))
outfile.write("Total hours worked     {0:6.2f}\n\n".format(totHours))
outfile.write("{0:>3d} records processed".format(recno))

outfile.close()
