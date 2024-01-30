def triangle(n):
  k = n - 8
  for i in range(9,n):
    for j in range(8,k):
      print(end = " ")
    k -= 7
    for j in range (7, i+1):
      print("* ", end='')
    print("\n") 

n = int(input())
triangle(n)
