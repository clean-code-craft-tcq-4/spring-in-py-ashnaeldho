#from statistics import mean
#from functools import reduce
#import math
def calculateStats(numbers):
  length_1 = len(numbers);
  
    
  print(numbers)
  if list(numbers) == 0:
    break;
  else:
    total = sum(map(float,numbers));
  
  
 
  #total = sum(map(float,numbers));
  print("total :", total);
  avg = total/length_1;
  #avg = mean(numbers);
  #avg = reduce(lambda x, y: x + y, numbers) / len(numbers)
  print("average :", avg);
  
  max_num = max(numbers);
  print("max value :", max_num);
  min_num = min(numbers);
  print("min value :", min_num);
  return avg, max_num, min_num
