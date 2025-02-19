n = int(input())
nets = list(map(int, input().split()))
connection = dict()
nums = [i for i in range(1, n + 1)]
for i in range(0, len(nets), 2):
    if nets[i] not in connection.keys():
        connection[nets[i]] = list()
    connection[nets[i]].append(nets[i + 1])
    if nets[i] in nums:
        nums.remove(nets[i])

if len(nums) == 1:
    judge = nums[0]
    for i in range(1, n + 1):
        if i == judge or judge in connection[i]:
            continue
        else:
            judge = -1
            break
    print(judge)
else:
    print('-1')