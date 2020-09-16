ham = 4321

def spam():
    global ham
    ham = 5432
    eggs = 1234
    print(ham)

spam()
print(ham)
print(eggs)

