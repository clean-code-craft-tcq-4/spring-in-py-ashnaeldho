#import 
#def calculateStats(numbers):
#  length_1 = len(numbers);
  
    
#  print(numbers)
#  while(1):
#    if (list(numbers) or len(numbers)) != 0:
#      total = sum(map(float,numbers));
#      avg = total/length_1;
    
 #   else:
  #    continue
  
  
 
  
  #print("total :", total);
 
  #print("average :", avg);
  
  #max_num = max(numbers);
  #print("max value :", max_num);
  #min_num = min(numbers);
  #print("min value :", min_num);
  #return avg, max_num, min_num

import math as m

def calculateStats(numbers):
  if type(numbers) == list:
    l = len(numbers)
    for i in range(l):
      if type(numbers[i]) == str:
        value = m.isnan(i)
        return value
      elif (type(numbers[i]) == float) or (type(numbers[i]) == int) and (l != 0):
        avgVal = sum(numbers) / l
        maxVal = max(numbers)
        minVal = min(numbers)
        return avgVal,minVal,maxVal
