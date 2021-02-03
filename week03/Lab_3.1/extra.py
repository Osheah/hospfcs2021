# why does this expression cause problems and what is the fix
# helen o'shea
# 20210203
try: 
  message = 'I have eaten ' + 99 +' burritos.'
except: 
   message = 'I have eaten ' + str(99) +' burritos.' 
print(message)
