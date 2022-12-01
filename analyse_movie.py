import json
analyse=open("savemovies.json","r")
saved_movies=json.load(analyse)
analyse.close()

# print(len(saved_movies))
point=0
point1=0
point2=0
point3=0
point4=0
point5=0



for x in range(len(saved_movies)):
     
    # print (saved_movies[x])
    if saved_movies[x]["genre"]=="Comedy":
        point+=1
        # print("comedy point")
    elif saved_movies[x]["genre"]=="Thriller":
        point1+=1
        # print("thriller point")
    elif saved_movies[x]["genre"]=="Action":
        point2+=1
        # print("action point")
    elif saved_movies[x]["genre"]=="Horror":
        point3+=1
        # print("horror point")
    elif saved_movies[x]["genre"]=="Animation":
        point4+=1
     # print("animation point")
    elif saved_movies[x]["genre"]=="Romance":
        point5+=1
        # print("romance point")

   
# print(max(point,point1,point2,point3,point4,point5))
print(" comedy has",point,"views.\n",
"thriller has ",point1,"views.\n",
"action has",point2,"views.\n",
"horror has",point3,"views.\n",
"animation has",point4,"views.\n",
"romance has",point5,"views.\n")


for x in saved_movies:
    age=[]
    print(x["Age"])
    if x["Age"]>=18:
        print(x["Username"],"is within 18-25 age range")
        age.append(x["Age"])
    elif x["Age"]<=25:
        print(x["Username"],"is within 18-25 age range")
    elif x["Age"]>=26:
        print(x["Username"],"is within 26-30 age range")
        age.append(x["Age"])
    elif x["Age"]<=30:
        print(x["Username"],"is within 26-30 age range")
    elif x["Age"]>=40:
        print(x["Username"],"is within 40-50 age range")
        age.append(x["Age"])
    elif x["Age"]<=50:
        print(x["Username"],"is within 40-50 age range")
    
    elif x["Age"]>=60:
        print(x["Username"],"is within 60 and above age range")
        age.append(x["Age"])
    else:
        print("your age_range is not in our database")


  
    
# age_range=["18-25","26-30","40-50","60-above"]
# print(age_range[0])
# for y in saved_movies:
#         apoint=0
#         apoint1=0
#         apoint2=0
#         apoint3=0
# print(y["Age"])
# if saved_movies[x]["Age"]>=18:
#     apoint+=1
# elif saved_movies[x]["Age"]<=25:
#     apoint+=1


#     # print(x["Username"]," of",saved_movies[x]["Age"],"years of Age likes",x["genre"])

# elif saved_movies[x]["Age"]>=26 :
#     apoint1+=1
# elif saved_movies[x]["Age"]<=30:
#     apoint1+=1
    # print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"])
# elif saved_movies[x]["Age"]>=40 :
#     apoint2+=1

# elif saved_movies[x]["Age"]<=50:
#     apoint1+=1

# elif saved_movies[x]["Age"]>=60:
#     apoint3+=1
# else:
#     print("sorry!",saved_movies[x]["Username"],"you are not within our age range")

# print(apoint,apoint1,apoint2,apoint3)


# fpoint=0
# fpoint1=0
# fpoint2=0
# fpoint3=0
# fpoint4=0
# fpoint5=0


# mpoint=0
# mpoint1=0
# mpoint2=0
# mpoint3=0
# mpoint4=0
# mpoint5=0




# if saved_movies[x]["Gender"]=="F":
#                                 if saved_movies[x]["genre"]=="Comedy":
                    
#                                         fpoint+=1
#                                         print(saved_movies[x]["Gender"],",has comedy point",fpoint)
#                                 elif saved_movies[x]["genre"]=="Thriller":
#                                          fpoint1+=1
#                                          print(saved_movies[x]["Gender"],",has thriller point",fpoint1)
#         # print("thriller point")
#                                 elif saved_movies[x]["genre"]=="Action":
#                                          fpoint2+=1
#                                          print(saved_movies[x]["Gender"],",has action point",fpoint2)
#         # print("action point")
#                                 elif saved_movies[x]["genre"]=="Horror":
#                                         fpoint3+=1
#                                         print(saved_movies[x]["Gender"],",has horror point",fpoint3)
#                                         # print("horror point")
#                                 elif saved_movies[x]["genre"]=="Animation":
#                                         fpoint4+=1
#                                         print(saved_movies[x]["Gender"],",has animation point",fpoint4)
#                                         # print("animation point")
#                                 elif saved_movies[x]["genre"]=="Romance":
#                                         fpoint5+=1
#                                         print(saved_movies[x]["Gender"],",has romance point",fpoint5)
#                                         # print("romance point")

                                
#                                 # print(max(point,point1,point2,point3,point4,point5))
#                                 print("comedy appears:",fpoint,"times.",
#                                 "thriller appears:",fpoint1,"times.",
#                                 "action appears:",fpoint2,"times.",
#                                 "horror appears:",fpoint3,"times.",
#                                 "animmation appears:",fpoint4,"times.",
#                                 "romance appears:",fpoint5,"times.")

# elif saved_movies[x]["Gender"]=="M":
#                                 if saved_movies[x]["genre"]=="Comedy":
                    
#                                         mpoint+=1
#                                         print(saved_movies[x]["Gender"],",has comedy point",mpoint)
#                                 elif saved_movies[x]["genre"]=="Thriller":
#                                         mpoint1+=1
#                                         print(saved_movies[x]["Gender"],",has thriller point",mpoint1)
#         # print("thriller point")
#                                 elif saved_movies[x]["genre"]=="Action":
#                                     mpoint2+=1
#                                     print(saved_movies[x]["Gender"],",has action point",mpoint2)
#                                     # print("action point")
#                                 elif saved_movies[x]["genre"]=="Horror":
#                                     mpoint3+=1
#                                     print(saved_movies[x]["Gender"],",has horror point",mpoint3)
#                                     # print("horror point")
#                                 elif saved_movies[x]["genre"]=="Animation":
#                                     mpoint4+=1
#                                     print(saved_movies[x]["Gender"],",has animation point",mpoint4)
#                                     # print("animation point")
#                                 elif saved_movies[x]["genre"]=="Romance":
#                                     mpoint5+=1
#                                     print(saved_movies[x]["Gender"],",has romance point",mpoint5)
#                                     # print("romance point")

                            
                            # print(max(point,point1,point2,point3,point4,point5))
                            #     print("comedy appears:",point,"times.",
                            # "thriller appears:",point1,"times.",
                            # "action appears:",point2,"times.",
                            # "horror appears:",point3,"times.",
                            # "animmation appears:",point4,"times.",
                            # "romance appears:",point5,"times.")




    # print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"])

# elif x["Age"]<=26: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
    
# elif x["Age"]<=40: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
       
# elif x["Age"]>=60: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
# else:
         
#         print("sorry",x["Username"]," of",x["Age"],"years of Age you are not in our age range")
    

# print(analyse_list)

# genrelist=open("genre.json","r")
# genre=json.load(genrelist)
# # print(genre)

# customerlist=open("try.json","r")
# customer=json.load(customerlist)
# print(customer)
# age_range1="18-15"
# age_range2="26-30"
# age_range3="40-50"
# age_range4="60"
# for x in saved_movies:
#     if x["Age"]<=18: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
    
#     elif x["Age"]<=26: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
    
#     elif x["Age"]<=40: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
       
#     elif x["Age"]>=60: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
#     else:
         
#         print("sorry",x["Username"]," of",x["Age"],"years of Age you are not in our age range")
    
    
# genre[0]="Comedy"
# genre[1]="Thriller"
# genre[2]="Action"
# genre[3]="Horror"
# genre[4]="Animation"
# genre[5]="Romance"

# def funny():
#     for x in saved_movies:
#         for y in customer:
            
#                 if x["Username"]==y["Email"]:
#                     print(x["Username"])
#                 operation(x)
# def operation(x):
#     point=0
#     if x["genre"]["genre1"]==genre[0]:
#         print("true1")
#     if x["genre"]["genre2"]==genre[0]:
#         point+=1
#         print("true2")
#     if x["genre"]["genre3"]==genre[0]:
#         print("true3")
#         point+=1

#     if x["genre"]["genre1"]==genre[1]:
#         print("true4")
#         point+=1
#     if x["genre"]["genre2"]==genre[1]:
#         print("true5")
#         point+=1
#     if x["genre"]["genre3"]==genre[1]:
#         print("true6")
#         point+=1
    
#     if x["genre"]["genre1"]==genre[2]:
#         print("true7")
#         point+=1
#     if x["genre"]["genre2"]==genre[2]:
#         print("true8")
#         point+=1
#     if x["genre"]["genre3"]==genre[2]:
#         point+=1
#         print("true9")
    
#     if x["genre"]["genre1"]==genre[3]:
#         point+=1
#         print("true0")
#     if x["genre"]["genre2"]==genre[3]:
#         point+=1
#         print("true11")
#     if x["genre"]["genre3"]==genre[3]:
#         print("true12")
#         point+=1

#     if x["genre"]["genre1"]==genre[4]:
#         point+=1
#         print("true13")
#     if x["genre"]["genre2"]==genre[4]:
#         print("true14")
#         point+=1
#     if x["genre"]["genre3"]==genre[4]:
#         point+=1
#         print("true15")
    
#     if x["genre"]["genre1"]==genre[5]:
#         print("true16")
#         point+=1
#     if x["genre"]["genre2"]==genre[5]:
#         print("true17")
#         point+=1
#     if x["genre"]["genre3"]==genre[5]:
#         point+=1
#         print("true18")
#     # print(point)
    
    


# funny()
        
            
    

        # print(x["genre"]["genre1"])
        # print(y) 