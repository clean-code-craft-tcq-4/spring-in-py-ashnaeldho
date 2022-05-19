#from statistics import mean
def calculateStats(numbers):
  length_1 = len(numbers);
  sum = 0;
  for n in numbers:
    sum = sum + numbers[n];
  avg = sum/length_1; 
  #avg = mean(numbers);
  max = max(numbers);
  min = min(numbers);
  return avg, max, min
