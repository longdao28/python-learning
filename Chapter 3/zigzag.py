import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True #Whether the indentation is increasing

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Chage direction
                indentIncreasing = False

        else:
            # Decrease number of spaces
            indent = indent - 1
            if indent == 0:
                # Chage direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
