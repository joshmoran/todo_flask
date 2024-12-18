import datetime

# Creating and Evaluating time 

date = '2024-12-17'
time = '12:05:32'

dateArray = date.split('-')
timeArray = time.split(':')

taskYear = int(dateArray[0])
taskMonth = int(dateArray[1])
taskDay = int(dateArray[2])

taskHour = int(timeArray[0])
taskMinute = int(timeArray[1])
taskSecond = int(timeArray[2])

currentDateTime = datetime.datetime(taskYear, taskMonth, taskDay, taskHour, taskMinute, taskSecond)

# Current Time
currentTime = datetime.datetime.now()


between = currentTime - currentDateTime

minutes = between.total_seconds() / 60
seconds = between.seconds / 60
def formatNumber( num ):
  return "{:.0f}".format(abs(num ))

if between.days == -1:
  days = between.days
  hours = formatNumber( minutes / 60 )
  minutes = formatNumber( minutes % 60 )
  seconds = formatNumber( seconds % 60 )
 
  print( seconds )
  print(f"The time remaining is {hours} hours, {minutes} minutes and {seconds} seconds")
else:
  days = formatNumber( between.days )
  hours = formatNumber( minutes % 60 )
  minutes = formatNumber( minutes % 60 )
  seconds = formatNumber( seconds % 60 )
 
  print(f"The time remaining is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")


