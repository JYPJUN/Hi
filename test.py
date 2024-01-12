#%%
sum = int(input())
n = int(input())
total_sum = 0

for i in range(n):
    value, count = map(int, input().split())
    total_sum += value * count

if sum == total_sum:
    print('Yes')
elif sum != total_sum:
    print('No')

# %%
