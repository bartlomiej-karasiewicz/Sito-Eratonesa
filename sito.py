def sito(x):
   a = [True] * (x + 1)
   for i in range(2, x + 1):
       if a[i] == False:
           continue
       for j in range(i*i, x+1, i):
           a[j] = False
   return [i for i in range(2, x + 1) if a[i] == True]

x=int(raw_input('Podaj zakres:'))
print sito(x)