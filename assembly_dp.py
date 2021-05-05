import time

def carAssemblyRecursion(a, t, e, x):
    # a cost array
    # t tranfer cost
    # e entry time
    # x exit time
  def recur(i,j):
    if i==0 and j==0:
      return a[0][j]+e[0]
    if i==1 and j==0:
      return a[1][j]+e[1]
    if i==0:
      return min(recur(0,j-1),recur(1,j-1)+t[1][j])+a[0][j]
    if i==1:
      return min(recur(1,j-1),recur(0,j-1)+t[0][j])+a[1][j]

  f1 = recur(0,len(a[0])-1)
  f2 = recur(1,len(a[0])-1)
  return min(f1+x[0],f2+x[1])

def carAssemblyDP(a, t, e, x):
    # a cost array
    # t tranfer cost
    # e entry time
    # x exit time
    NUM_STATION = len(a[0])

    dp = [[0 for _ in range(NUM_STATION)] for i in range(2)] 

    dp[0][0] = a[0][0] + e[0]
    dp[1][0] = a[1][0] + e[1]

    for i in range(1,NUM_STATION):
      dp[0][i] = min(dp[0][i-1],dp[1][i-1]+t[1][i])+a[0][i]
      dp[1][i] = min(dp[1][i-1],dp[0][i-1]+t[0][i])+a[1][i]

    return min(dp[0][NUM_STATION-1]+x[0],dp[1][NUM_STATION-1]+x[1])
    

a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]] 
e = [10, 12]
x = [18, 7]


start_time = time.time()
print(carAssemblyRecursion(a,t,e,x))
print("--- %s seconds ---" % (time.time() - start_time))