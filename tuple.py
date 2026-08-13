#A tuple is an ordered, immutable collection of items

animes = ("Naruto",'one piece','Aot','Demon Slayer')
print(animes)
print (animes[0])
#animes[0]= "boruto" this will give error 

# tuples are used when you have data that should not change ex dob,student id ,employee id ,gps coordinates etc 

#tuple packing and unpacking 

student =  ('Ansh','24CE100',19)
name,id,age = student 
print(name)
print(id)
print(age)