# This program says hello and asks for my name and give out the length of my name, show my age in 1 year later.

print('Hello, world!')
print('What is your name?') #ask for their name
myName = input()
print('Nice to meet you, ' + myName)
print('Length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in 1 year from now')

