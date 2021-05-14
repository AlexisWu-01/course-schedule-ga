# Course Scheduling with Genetic Algorithm
## Introduction
Course scheduling requires lots of considerations, from time slots on different weekdays to professor and classroom assignment. We also need to adjust for student preference: they take some course combinations together.  It certainly takes loads of time and brain to make the perfect decision but we could use computers to help us. Here we are using genetic algorithm to help school registrar generate a course schedule that makes most of the students and staff happy.

## To-Run
### Dependencies:
pip install
- pandas
- numpy
- xlwt, xlrd (For sheet processing)

## Files and Output
- instructor.csv: serves as pid table in database, links teacher id with their names.
- courseinfo.csv: links course id with their names.
- plan.csv: for groups, used for bundle classes together: like ModSim and ISIM
- academic_calendar.csv: shows dates of class occurance.


You just need to run <br>`python main.py`. 

Then the generated course schedule would be saved to arrangement.csv.

If you need to change input of class, just modify the input files and numbers defined in head in main.py (like count of courses, number of intructors).

