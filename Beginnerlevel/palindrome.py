try :
  x=int(input())
  y=str(x)
  y=y[::-1]
  z=int(y)
  if x==z :
    print("yes")
  else :
    print("no")
except :
  print ("Invalid input")
