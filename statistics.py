
def calculateStats(numbers):
  length_1 = len(numbers);
  
    
  print(numbers)
  while(1):
    if (list(numbers) or len(numbers)) != 0:
      total = sum(map(float,numbers));
      avg = total/length_1;
    
    else:
      continue
  
  
 
  
  print("total :", total);
 
  print("average :", avg);
  
  max_num = max(numbers);
  print("max value :", max_num);
  min_num = min(numbers);
  print("min value :", min_num);
  return avg, max_num, min_num


