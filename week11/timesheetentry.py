# programme to create a timesheet entry class
# # helen oshea
# 20210430
import datetime as dt
class Timesheetentry:
  def __init__(self, project, start, duration):
    self.project = project
    self.start = start
    self.duration = duration
  def __str__(self):
    return self.project + ':' + str(self.duration)  

if __name__=='__main__':
  ts = dt.datetime(2021, 4, 30, 10, 32)    
  test = Timesheetentry('test', ts, 60)
  print(test)
