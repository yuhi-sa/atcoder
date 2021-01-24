import numpy as np

n = int(input())
MOD = 1000000007
ans = 10**n - 9**n -9**n + 8**n
ans = ans % MOD
print(ans)
