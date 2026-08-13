#Lists and tuples are data structures in Python used to store multiple values in a single variable.
#A list is an ordered, mutable collection of items.

animes = ["Naruto",'one piece','Aot','Demon Slayer']
print(animes)
print(animes[0])
animes[0] = 'Boruto' #lists are mutable so we can change their elements even  after creating them
print(animes[0])
animes.append("jjk")  #adds element at the end 
animes.insert(2,'Bleach')  #adds element at particular index
print(animes)
animes.remove("Boruto")  # removes the element
animes.pop()  #removes the last element from the list
print(animes)

#nested list 

matrix = [
 ['Ansh',100],
 ['shivam',98] ,
 ['vijaY',99]
]
#dont forget commas between lists
print(matrix)
print(matrix[0][0])