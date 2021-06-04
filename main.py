import pyperclip 
import sys

if len(sys.argv) > 1:
# Get message from command line.
    message = ' '.join(sys.argv[1:])
else:
# Get message from clipboard.
    message = pyperclip.paste()

crooked_message = []
chars = list(message)
switch = 1

for char in chars:
    if switch == 0:
        crooked_message.append(char.lower())
        switch = 1
    elif switch == 1:
        crooked_message.append(char.upper())
        switch = 0


output = ''.join(crooked_message)
pyperclip.copy(output)

pyperclip.copy(output)
print("Your cRoOkEd message is '" + output + "' and it has been copied to your clipboard, so you're welcome.")