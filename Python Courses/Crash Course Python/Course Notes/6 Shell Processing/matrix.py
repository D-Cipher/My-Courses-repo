#Programming Fundementals: Python Shell

#Program that simulates the matrix scene.
def matrix():
  print("Wake up,")
  print("your name...")
  name = input()
  print("The Matrix has you.")
  print("Follow the white rabbit.")
  response = input()
  knock = "Knock, knock... " + name + "."
  print(knock)
  
matrix()
  
#save program as matrix.py 
#in Shell following to access:
#exec(open(".../matrix.py").read())