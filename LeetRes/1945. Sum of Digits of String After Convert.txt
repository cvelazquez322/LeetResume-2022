def alphaTranslator(alpha):
    string2return = ""
    if alpha == "a":
        string2return = "1"
    if alpha == "b":
        string2return = "2"
    if alpha == "c":
        string2return = "3"
    if alpha == "d":
        string2return = "4"
    if alpha == "e":
        string2return = "5"
    if alpha == "f":
        string2return = "6"
    if alpha == "g":
        string2return = "7"
    if alpha == "h":
        string2return = "8"
    if alpha == "i":
        string2return = "9"
    if alpha == "j":
        string2return = "10"
    if alpha == "k":
        string2return = "11"
    if alpha == "l":
        string2return = "12"
    if alpha == "m":
        string2return = "13"
    if alpha == "n":
        string2return = "14"
    if alpha == "o":
        string2return = "15"
    if alpha == "p":
        string2return = "16"
    if alpha == "q":
        string2return = "17"
    if alpha == "r":
        string2return = "18"
    if alpha == "s":
        string2return = "19"
    if alpha == "t":
        string2return = "20"
    if alpha == "u":
        string2return = "21"
    if alpha == "v":
        string2return = "22"
    if alpha == "w":
        string2return = "23"
    if alpha == "x":
        string2return = "24"
    if alpha == "y":
        string2return = "25"
    if alpha == "z":
        string2return = "26"
    return string2return
# expects numeric characters currently in string form:
# returns addition of this strings in str form
def alphanumeral2num(alpha):
    alphalist = list(alpha)
    num = 0
    for string in alphalist:
        num += int(string)
    return str(num)
    def alpha2numalpha(alpha, itter):
    alphalist = list(alpha)
    numstring = ""
    for alpha in alphalist:
        #print(alphaTranslator(alpha))
        #print(numstring)
        numstring += alphaTranslator(alpha)
    while itter != 0:
        numstring = alphanumeral2num(numstring)
        itter -= 1
    return numstring
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        if s == "":
            return 0
        s = s.lower()
        return alpha2numalpha(s, k)