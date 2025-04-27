numbers = [3, 5, 10, 14, 20, 22, 25]

# filter-ის გამოყენებით 5-ზე უნაშთო გაყოფა
multiples_of_five = list(filter(lambda x: x % 5 == 0, numbers))

print(multiples_of_five)
