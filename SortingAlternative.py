def alternateSort(arr, n): 
    arr.sort()  
    i = 0
    j = n-1
      
    while (i < j):  
      
        print(arr[j], end =" ") 
        j-= 1
        print(arr[i], end =" ") 
        i+= 1
  
    if (n % 2 != 0): 
        print(arr[i])  
  
  
if __name__=="__main__":
    arr = [1, 6, 9, 4, 3, 7, 8, 2]  
    n = len(arr) 
    
    alternateSort(arr, n)  