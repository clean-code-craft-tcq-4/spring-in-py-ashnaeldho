#from statistics import mean
#import math
def calculateStats(numbers):
  length_1 = len(numbers);
  #total = 0;
  #if type(numbers) == list:

    #print("a is a list")

  #else:

    #print("a is a tuple")
    
  print(numbers)
  #for ele in range(0, len(numbers)):
    #total = total + numbers[ele]
  #sum = 0;
  #for n in numbers:
  #  sum = sum + numbers[n];
    
  
  #for element in range(len(numbers)):
  #      numbers[element]=float(numbers[element])
  #      numbers[element]=math.pow(numbers[element],2)
  #total=sum(numbers[0:element+1])
  #avg = total/length_1; 
  total = sum(map(float,numbers));
  avg = total/length_1;
  print("average :", avg);
  #print("index of average : ", avg.index);
  #avg = sum(numbers);
  max_num = max(numbers);
  print("max value :", max_num);
  min_num = min(numbers);
  print("min value :", min_num);
  return avg, max_num, min_num
