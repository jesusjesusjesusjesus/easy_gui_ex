import easygui

nz_word = easygui.enterbox("Please enter the NZ word", "Word to check")
letters = list(nz_word)
spell_checked = False
letter_pos = 0
spell_corrected = ""
corrected = False


while spell_checked is False:
    if "u" is in letters:
        letter_pos = letters.index("u")
        if letter_pos + 1 == "r" and letter_pos - 1 == "o":
            letters.remove(letter_pos)
            spell_corrected = ["our", "or"]
            corrected = True
    if "s" is in letters:
        letter_pos = letters.index("s")
        if letter_pos + 1 == "i" and letter_pos - 1 == "e":
            letters.replace(letter_pos, "z")
            spell_corrected = ["ise", "ize"]
            corrected = True
        if letter_pos + 1 == "y" and letter_pos - 1 == "e":
            letters.replace(letter_pos, "z")
            spell_corrected = ["yse", "yze"]
            corrected = True
    else:
        corrected = False
        spell_checked = False



if corrected == True:
    easygui.msgbox(f"The American spelling of {nz_word} is {''.join(letters)}",
               "Result")
if corrected == False:
    easygui.msgbox(f"there is no change in spelling")
