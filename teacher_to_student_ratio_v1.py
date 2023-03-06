import random

import easygui
from easygui import *

output = []
function = False
left_over_kids = 0
kids_per_class = 0
number_of_classes = 0
number_of_classes_wo_teacher = 0
kids_div = 0
kids_floor = 0
left_over_kids_div = 0

while function == False:
    text = "Enter the following details"
    title = "data input"
    input_list = ["school name", "max kids per class", "school total", "number of teachers"]
    default_list = ["eg middleton grange", "between 10 and 30", "between 10 and 1400", "between 1 and 120"]
    output = multenterbox(text, title, input_list, default_list)
    if output[0] == "eg middleton grange":
        function = False
        easygui.msgbox("please change all of the values")
    if output[1] == "max kids per class":
        function = False
        easygui.msgbox("please change all of the values")
    if output[2] == "school total":
        function = False
        easygui.msgbox("please change all of the values")
    if output[3] == "number of teachers":
        function = False
        easygui.msgbox("please change all of the values")
    else:
        kids_per_class = output[2] // output[1]

        # fix this maths
        number_of_classes = output[2] / output[1]
        number_of_classes_wo_teacher = number_of_classes - output[3]
        left_over_kids_div = number_of_classes_wo_teacher * output[1]
        if (left_over_kids_div / 1) > (left_over_kids_div // 1):
            left_over_kids = left_over_kids_div // 1 + 1
        if kids_per_class > output[3]:
            easygui.msgbox(f"there are not enough teachers\nthere would be {left_over_kids} unaccounted for")
