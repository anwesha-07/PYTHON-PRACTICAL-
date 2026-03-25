def digit_sum(num):
    return sum(int(d) for d in num)
s = "123 45 9 10 2 100"
nums = s.split()

ds = [digit_sum(num) for num in nums]

max_len = 1
curr_len = 1
start = 0
max_start = 0
for i in range(1, len(nums)):
    if ds[i] > ds[i - 1]:
        curr_len += 1
    else:
        if curr_len > max_len:
            max_len = curr_len
            max_start = start
        curr_len = 1
        start = i
if curr_len > max_len:
    max_len = curr_len
    max_start = start
result = nums[max_start:max_start + max_len]

print("Longest Increasing Digit-Sum Subsequence:", result)
print("Length:", max_len)