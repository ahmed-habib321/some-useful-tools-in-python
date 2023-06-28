import os
import webbrowser

try:
    p1 = ""    
    p2 = ""
    p3 = ""
    webbrowser.open(p1)
    webbrowser.open(p2)
    webbrowser.open(p3)
except BaseException as ex:
    print(ex)
    input("finish")
    



