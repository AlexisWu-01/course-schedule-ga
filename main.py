# coding: utf-8

import numpy as np
from csv import *
from xlwt import *
from xlrd import *
from genetic import *
from pandas import *
c_count=8
student_groupnum=5
profnum=9
course_prof=[]

classdetailfile=open('courseinfo.csv','r',encoding='gbk')
classdetail=DictReader(classdetailfile)
courseid={}
for item in classdetail:
    courseid[item['classID']]=item['classID']
    
classdetailfile=open('courseinfo.csv','r')    
detail=DictReader(classdetailfile)
courses=[row['classID'] for row in detail]

proffile=open('instructor.csv','r')
profdetail=DictReader(proffile)
profid={}
for item in profdetail:
    profid[item['Id']]=item['Name']

with open('instructor.csv') as f:
    r=reader(f)
    data=list(r)
    for c_count in range(1,c_count+1):
        L=[]
        for tid in range(1,profnum+1):
            if data[tid][c_count+1]=='1':
                L.append(tid)
        course_prof.append(L)

s=[]
data=[]
with open('plan.csv') as f:
    r=reader(f)
    data=list(r)
    for student_group in range(1,student_groupnum+1):
        for c_count in range(1,c_count+1):
            # print(data)
            for i in range(int(data[c_count][student_group])):
                tid=np.random.randint(0, len(course_prof[c_count-1]), 1)[0]
                s.append(Schedule(data[c_count][0], student_group,course_prof[c_count-1][tid]))

ga = GeneticOptimize()
res = ga.evolution(schedules=s, roomRange=5,slotnum=19)

col_labels = ['weekNu5mber','weekStart','weekEnd','Mon','Tue','Wed','Thu','Fri','Sat','Sun']
size=len(col_labels)
w=Workbook(encoding = 'ascii')
style = XFStyle()
style.alignment.wrap = 1
style.alignment.vert = 1
style.alignment.horz = 2
with open('academic_calendar.csv') as calendar:
    #re=reader()
    r = calendar.readlines()
    for i in range(len(r)):
        r[i] = r[i].split(',')
    for student_group in range(1,student_groupnum+1):
        sheet=w.add_sheet(data[0][student_group])
        for i in range(11):
            sheet.col(i).width=256*13
        for j in range(size):
            sheet.write(0,j,col_labels[j],style)
        for j in range(1,20):
            for k in range(3):
                sheet.write(j,k,r[j][k],style)
        schedule = []
        for k in res:
            if k.classId == student_group:
                schedule.append(k)
        for s in schedule:
            weekDay = s.weekDay
            slot = s.slot
            
            text = str(courseid[s.courseId])+'\location-'+ 'AC' + str(s.roomId)+'\ntaughtby：'+str(profid[str(s.profID)])
            sheet.write(slot,weekDay+2,text,style)
                
w.save('arragement.csv')