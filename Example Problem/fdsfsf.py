def maxaverage(l):
  players=[]
  scores = []
  noi = []
  avg = []
  for i in range(len(l)):
      x = l[i][0]
      if x in players:
          j=players.indexof(x)
          scores[j] += l[i][1]
          noi[j]+= 1
      else:
          players.append(x)
          scores.append(l[i][1])
          noi.append(i)
  res=[]
  for i in range(len(scores)):
      average.append((float(scores[i])/noi[i])
      res = [x for _,x in sorted(zip(avg,players))]
  return(res)
