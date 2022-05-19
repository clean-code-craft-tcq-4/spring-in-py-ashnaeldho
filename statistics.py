#from statistics import mean
import math
def calculateStats(numbers):
  length_1 = len(numbers);
  
  #sum = 0;
  #for n in numbers:
  #  sum = sum + numbers[n];
    
  for element in range(len(numbers)):
        numbers[element]=float(numbers[element])
        numbers[element]=math.pow(numbers[element],2)
  total=sum(numbers[0:element+1])
  avg = total/length_1; 
  #avg = mean(numbers);
  max = max(numbers);
  min = min(numbers);
  return avg, max, min
