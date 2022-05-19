from statistics import mean
def calculateStats(numbers):
  
  avg = mean(numbers);
  max = max(numbers);
  min = min(numbers);
  return avg, max, min
