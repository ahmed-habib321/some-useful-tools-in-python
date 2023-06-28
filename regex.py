import re

def ismatch(pattern , text):
    return not ( None == re.match(pattern=pattern , string=text))

try:

    # patt = "([A-Z]?[a-z]+){3}\s"
    # text = "Ahmed mohamed abdelsalam"

    # patt = "([+20]|[0]|())[0-9]{10}"      
    # text = "+201234567900"

    # patt = "[a-z].*[a-z]"      
    # text = "a☻g"

    patt = "[a-z].+[a-z]"      
    text = "a≥«g"
    print(ismatch(patt,text))
    

except BaseException as ex:
    print(ex)
    

input("fin")