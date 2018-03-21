try :
  x=int(input())
  n=0
  for i in range(2,x):
    if(x%i==0) :
     n=n+1
  if n==0 :
    print ("yes")
  else :
    print("no")
    
  
except :
  print ("Invalid input")
