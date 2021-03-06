# Name: Aaqib Ismail
# Email: aaqibismail@gmail.com

# Schedule-Maker

Scheduling classes is a hassle especially when the school year is already underway.
While most students know which classes they want to take, it's often tiresome to manually
check back and forth whether class times will overlap or not. This website is aimed at
dealing this. Unfortunately, scheduling problems are NP-hard making this project WIP.

The back-end is a python server which uses a USC API to read in the data about each course
available at USC. 

Features to Implement:
 - Develop a scheduling algorithm that can dynamically create possible combinations without
   an inefficient brute-force method. Link below shows another scheduling system during actual
   selection rather than simply having the user give input
   https://github.com/jonluca/USC-Schedule-Helper/blob/master/USCScheduleHelper.js

 - Allow user to specify starting and ending time of days

 - Give give user the option to not schedule classes on Fridays

 - Include average Rate My Professor Rating

 - Rank schedules by user preference such as by Rate My Professor Rating or time