import random 
values = [random.randint(1, 5) for i in range(3)]
weight = [random.randint(0, 5) for i in range(3)]
print(values, weight)
sum_weight = []
for i in range(len(weight)):
  for j in range(weight[0]):
    sum_weight += values[0]
print(sum_weight)