# importing easygui module
from easygui import *

# message to be displayed
text = "Enter the following details"

# window title
title = "big box thang"

# list of multiple inputs
input_list = ["Name", "Class", "Section", "Address"]

# list of default text
default_list = ["walter", "XII", "A", "308 Negra Arroyo Lane, Albuquerque, New Mexico."]

# creating a integer box
output = multenterbox(text, title, input_list, default_list)

# title for the message box
title = "Message Box"

# creating a message
message = "Entered details are in form of list : " + str(output)

# creating a message box
msg = msgbox(message, title)
