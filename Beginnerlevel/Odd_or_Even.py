try :
    val=int(input())
    if val%2==0 and val<=100000:
    	print("Even")
    elif val%2==1 and val<=100000:
    	print("Odd")
    else :
      print("Invalid Input")
except  :
    print ("Invalid Input")
