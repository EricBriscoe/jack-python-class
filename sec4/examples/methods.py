pets = ["dog", "cat"]
print(pets.index("dog"))

pets.append("mouse")
print(pets)

pets.insert(2, "rabbit")
print(pets)

pets.remove("dog")
print(pets)

pets.sort()
print(pets)

pets.sort(reverse=True)
print(pets)


def second_letter(string):
    return string[1]


pets.sort(key=second_letter)
print(pets)
