import json
mydict={}
customer_list=[]
def signup():
    
    for x in range(5):
        Name=input("please enter your first and last name: ")
        Age=int(input("please enter your age: "))
        Gender=input("Enter your gender...M for Male, F for female: ")
        Email=input("please enter your email address: ")
        Password=input("please enter your desired password: ")
        details(Name,Age,Gender,Email,Password)
def details(Name,Age,Gender,Email,Password):    
        mydict={
                "Name":Name,
                "Age":Age,
                "Gender":Gender,
                "Email":Email,
                "Password":Password
             }
        customer(mydict) 
def customer(mydict):
        global customer_list    
        customer_list.append(mydict)
        print(customer_list)
        list=open("try.json","w")
        json.dump(customer_list,list,indent=4)
        list.close()    
           
signup()