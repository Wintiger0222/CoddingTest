n = int(input())


dp=[[]]*10
dp[0]=[0]*(n+1)
dp[1]=[0]*(n+1)
dp[2]=[0]*(n+1)
dp[3]=[0]*(n+1)
dp[4]=[0]*(n+1)
dp[5]=[0]*(n+1)
dp[6]=[0]*(n+1)
dp[7]=[0]*(n+1)
dp[8]=[0]*(n+1)
dp[9]=[0]*(n+1)


dp[0][1]=0
dp[1][1]=dp[2][1]=dp[3][1]=dp[4][1]=dp[5][1]=dp[6][1]=dp[7][1]=dp[8][1]=dp[9][1]=1


for i in range(2,n+1):
    dp[0][i]=dp[1][i-1]
    for j in range(1, 9):
        dp[j][i]=dp[j-1][i-1]+dp[j+1][i-1]
    dp[9][i]=dp[8][i-1]
    
print((dp[0][n]+dp[1][n]+dp[2][n]+dp[3][n]+dp[4][n]+dp[5][n]+dp[6][n]+dp[7][n]+dp[8][n]+dp[9][n])%1000000000)