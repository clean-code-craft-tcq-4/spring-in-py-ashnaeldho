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
  
 
  
  #print("total :", total);
 
  #print("average :", avg);
  
  #max_num = max(numbers);
  #print("max value :", max_num);
  #min_num = min(numbers);
  #print("min value :", min_num);
  #return avg, max_num, min_num




