#import 
import math as m
def calculateStats(numbers):
  if type(numbers) == list:
    length = len(numbers)
    for i in range(length):
      if type(numbers[i]) == str:
        value = m.isnan(i)
        return value
      elif (type(numbers[i]) == float) or (type(numbers[i]) == int) and (length != 0):
        avgVal = sum(numbers) / length
        maxVal = max(numbers)
        minVal = min(numbers)
        return avgVal,minVal,maxVal
      
def EmailAlert():
  emailAlertCallCount = 0
  emailAlertCallCount + = 1
  return emailAlertCallCount

def LEDAlert():
  ledAlertCallCount = 0
  ledAlertCallCount + = 1
  return ledAlertCallCount
     # elif (type(numbers[i]) == 0) or (type(numbers[i]) == 0) and (length = 0):
     #   avgVal = nan
     #   maxVal = nan
     #   minVal = nan
     #   return avgVal,minVal,maxVal
  
 




