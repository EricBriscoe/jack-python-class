import time

indent = 0
output = '******'
indentIncreasing = True

while True:
    print(' ' * indent, end='')
    print(output)

    if indentIncreasing:
        indent += 1  # The same as indent = indent + 1
        if indent > 20:
            indentIncreasing = False
    else: # indentDecreasing
        indent += -1
        if indent == 0:
            indentIncreasing = True
        

    time.sleep(.1)
