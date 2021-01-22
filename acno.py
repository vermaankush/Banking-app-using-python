from random import randint
ac=randint(5463200000, 5463299999)
ac2=randint(5463200000, 5463299999)
OTP=randint(00000,99999)
OTP2=randint(00000,99999)
def acc():
      print("Your account number is = ",ac)
def otp():
      print("Your OTP is = ",OTP)
def acc2():
      print("Your account number is = ",ac2)      
def otp2():
      print("Your OTP is = ",OTP2)
      
def email():
      q=1
      while q==1:
            em=input("Enter your E-mail ")
            if em.endswith("@gmail.com"):
                  q+=1
            else:
                  print("You have entered wrong E-mail")
                  print("Enter E-mail in format-abcd@gmail.com")
            
def login():
    print("Login page - \n")
    name3 = input("Enter your name ")
    pas3 = input("Enter your password ")
