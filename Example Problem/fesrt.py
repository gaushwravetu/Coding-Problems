def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
      x = l[i]
      if x<mymin:
          mythirdmin = mysecondmin
          mysecondmin = mymin
          mymin = x
      elif x<mysecondmin:
          mythirdmin = mysecondmin
          mysecondmin = x
      elif x<mythirdmin:
          mythirdmin = x
  return(mythirdmin)
