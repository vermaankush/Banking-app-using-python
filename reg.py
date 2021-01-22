from acno import *

def reg():
      print("You are a new user so u have to register below \n")
      print("Registration page - \n")

      register={
            "child1":{
                        "name":input("Enter your name "),
                        "phone":int(input("Enter your mobile number ")),    
                        "email":email(),
                        "addr":input("Enter your address "),
                        "pas":input("Enter your password "),
                        "ac":acc(),
                        "otp":otp()
                        },
            "child2":{
                        "name":input("Enter your name "),
                        "phone":int(input("Enter your mobile number ")),    
                        "email":email(),
                        "addr":input("Enter your address "),
                        "pas":input("Enter your password "),
                        "ac":acc2(),
                        "otp":otp2()
                        }
            }
      print("Login page - \n")
      i = 1
      t = 5
      global l
      while i<6:
                name2=input("Enter your name ")
                pas2=input("Enter your password ")
                n1=register["child1"].get("name")
                n2=register["child2"].get("name")
                p1=register["child1"].get("pas")
                p2=register["child2"].get("pas")
                if (name2==n1 and pas2==p1)or(name2==n2 and pas2==p2):
                    break
                else:
                    print("You have entered wrong details , you have only ",t-i," chances left ")
                    if t - i == 0:
                        l+=1
                
                i += 1
