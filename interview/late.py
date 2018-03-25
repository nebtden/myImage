def create_multipliers():
    return [lambda x : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))


for multiplier in (lambda x : i * x for i in range(5)):
    print(multiplier(2))