import json

userlist={}
savemovies=[]

def detail():
    customerlist=open("try.json","r")
    customer=json.load(customerlist)
     
    username=input("enter your email address: ")

    for y in customer:
    
        if y["Email"]==username:
           
            age=y["Age"]
            gender=y["Gender"]
            movie(username,age,gender)
            
        
def movie(username,age,gender):
    genrelist=open("genre.json","r")
    genre=json.load(genrelist)
    # print(genre)
    Genre=input("select a movie genre number:Comedy, Thriller,  Action,  Horror,  Animation, Romance: ")
   
    print(username,",",age,",",gender,", likes",Genre)
    userlist={
        "Username":username,
        "Age":age,
        "Gender":gender,
        "genre":Genre,
        
    }
    # print(userlist)


    savemovies.append(userlist)
    
# copy the details and save the persons details into a json file

    list=open("savemovies.json","w")
    json.dump(savemovies,list,indent=4)
    list.close()
def yeye():
    
    detail()
    
    if len(savemovies)==2:
            print("we don finish")
    else:
        yeye()

yeye()
        
    
        
    
    
