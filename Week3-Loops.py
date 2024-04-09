squares =["red", "yellow", "green", "purple","blue"]

for i in range(0,4):
     squares[i]="white"
     print(squares)

#make a for loop to turn all the squares ou a sequence to white

#for loop with enumerate() method
fruits = ['apple', 'banna', 'orange', 'strawberry']

for index, fruit in enumerate(fruits):
     print(f'at position {index}, i found a {fruit}')

otherSquares = ['orange', 'orange','purple','orange', 'blue']
NewSquares =[]
i=0

#While loops don't stop until the condition is false
while(otherSquares[i] =='orange'):
    NewSquares.append(otherSquares[i])
    i=i+1

print(NewSquares)
print(otherSquares)

#QUIZ

for x in range(0, 3):
    print(x)

for x in ['A', 'B', 'C']:
    print(x + 'A')

for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)
