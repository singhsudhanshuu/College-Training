print("Sudhanshu Singh")
def bs (arr, low,high, x):
    if high >= low:
        mid= (high+low)//2
        if arr [mid]==x:
            return mid 
        elif arr[mid]>x:
            return bs (arr,mid-1,x)
        else:
            return bs (arr,mid+1 ,high, x)
    else:
        return -1
arr = [ 3,5,6,7,81]
x=7
goal= bs (arr,0, len(arr)-1,x)
if goal!=-1:
    print ("Elment is at index", str (goal)) 
else:
    print ("Not in this one!!")