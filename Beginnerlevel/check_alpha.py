try :
  val = input("Input a letter of the alphabet: ").lower()
  if val in ('a', 'e', 'i', 'o', 'u','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z') :
	   print("Alphabet")
  else :
	   print("No")
except :
  print("No")
