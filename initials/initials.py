def get_initials(fullname):
    test_name = fullname.split()
    init = ""
    for name in test_name:
        init = init + name[0]
    return(init.upper())

def main(): 
    fullname = input("What is your full name? \n")
    print (get_initials(fullname))
    
    
if __name__=="__main__": 
    main()  