try :
    val=int(input())
    if val==0:
    	print("Zero")
    elif val<0:
	    print("Negative")
    elif val>0 and val<=100000:
    	print("Positive")
    else :
      print("Invalid Input")
except  :
    print ("Invalid Input")
