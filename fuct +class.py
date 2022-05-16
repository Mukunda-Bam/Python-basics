def child(*kid):
    print("my dada child name is " + kid[1]) #*args wala

child('laxmi', 'aavash')

def child(child1, child2):
    print('the youngest child is ' + child2)

child(child1='laxmi', child2='aavash')

def nation(country ="nepal"):  
    print("i am from " + country)

nation()
nation('usa')

#new funct
def eating(food): #for le tesai loop chalauxa .if hunapaye funct ko arg me number pass garnuparthyo
    
    for x in food:
        print(x)
    
fruits =['apple', 'ball', 'cat']
eating(fruits)
    