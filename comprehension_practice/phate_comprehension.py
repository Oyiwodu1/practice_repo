# A list comprehension is simply another way of writing that same idea in a shorter form.
numbers = []
for number in range(5):
    numbers.append(number)
    print(number)


def profile(**kwargs):
    print(kwargs)

profile(name="Faith")

print(kwargs)