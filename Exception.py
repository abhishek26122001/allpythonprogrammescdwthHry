# Keywords that will be used in EH are:
# 1. try  2. except  3. else  4. finally  5. raise


def ageVerification():
    try:
        age = int(input("Enter age: "))
        if age < 0:
            raise("Invalid")
        print(age)    
    except:
        print("Exception Caught")
        return None
    finally:
        print("Inside Finally Block")    
    print("No Exception")    
ageVerification()    