try :
  x=int(input())
  y=int(input())
  if x%2==0:
    for i in range(x,y-1,2):
      print(i+2)
  else :
    for i in range(x,y-2,2) :
      print(i+1)
except :
  print ("Invalid input")
