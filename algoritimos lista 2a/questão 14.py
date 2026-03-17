nums = []
for i in range(5):
    nums.append(int(input(f"Número {i+1}: ")))

media = sum(nums) / 5
print(f"Média: {media}")

for n in nums:
    if n > media:
        print(f"Maior que a média: {n}")