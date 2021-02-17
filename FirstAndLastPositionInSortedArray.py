def findFirstAndLast(arr, n, x) :
    first = -1
    last = -1
    for i in range(0, n) :
        if (x != arr[i]) :
            continue
        if (first == -1) :
            first = i
        last = i
     
    if (first != -1) :
        print( "First Occurrence = ", first, 
               " \nLast Occurrence = ", last)
    else :
        print("Not Found")
         
         
if __name__=="__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    n = len(arr)
    x = 5
    findFirstAndLast(arr, n, x)