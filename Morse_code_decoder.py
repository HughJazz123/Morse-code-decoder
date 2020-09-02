print("Morse code (. and -):") 
#has to type one by one
while True:
    a=input()
    if a==".-":
        print("A")
    elif a=="-...":
        print("B")
    elif a=="-.-.":
        print("C")
    elif a=="-..":
        print("D")
    elif a==".":
        print("E")
    elif a=="..-.":
        print("F")
    elif a=="--.":
        print("G")
    elif a=="....":
        print("H")
    elif a=="..":
        print("I")
    elif a==".---":
        print("J")
    elif a=="-.-":
        print("K")
    elif a==".-..":
        print("L")
    elif a=="--":
        print("M")
    elif a=="-.":
        print("N")
    elif a=="---":
        print("O")
    elif a==".--.":
        print("P")
    elif a=="--.-":
        print("Q")
    elif a==".-.":
        print("R")
    elif a=="...":
        print("S")
    elif a=="-":
        print("T")
    elif a=="..-":
        print("U")
    elif a=="...-":
        print("V")
    elif a==".--":
        print("W")
    elif a=="-..-":
        print("X")
    elif a=="-.--":
        print("Y")
    elif a=="--..":
        print("Z")
    elif a==".----":
        print("1")
    elif a=="..---":
        print("2")
    elif a=="...--":
        print("3")
    elif a=="....-":
        print("4")
    elif a==".....":
        print("5")
    elif a=="-....":
        print("6")
    elif a=="--...":
        print("7")
    elif a=="---..":
        print("8")
    elif a=="----.":
        print("9")
    elif a=="-----":
        print("0")
    elif a=="":
        print("\n"*40)
        
    else:
        print("Error: not found")
