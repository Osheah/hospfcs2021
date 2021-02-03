# program to take in currency dollar numbers (can be + or -) and converts it to cents
# helen o'shea
# 20210203

number = float(input('Pleas enter an amount: '))
convert = abs(number *100)
print('That (${}) amount in cent is {:.0f}c'.format(number, convert))
