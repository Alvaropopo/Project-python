import random
import numpy  as np

# List of 100 random words
random_words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'strawberry', 'blueberry', 'pineapple', 'peach',
                'lemon', 'lime', 'plum', 'pear', 'cherry', 'raspberry', 'blackberry', 'watermelon', 'mango', 'papaya',
                'apricot', 'avocado', 'coconut', 'fig', 'guava', 'kiwi', 'nectarine', 'pomegranate', 'date', 'dragonfruit',
                'elderberry', 'boysenberry', 'cranberry', 'grapefruit', 'kiwifruit', 'lychee', 'passionfruit', 'persimmon',
                'pumpkin', 'squash', 'zucchini', 'carrot', 'broccoli', 'cauliflower', 'spinach', 'kale', 'lettuce',
                'cucumber', 'bellpepper', 'tomato', 'onion', 'garlic', 'ginger', 'cinnamon', 'nutmeg', 'cloves', 'coriander',
                'cumin', 'turmeric', 'oregano', 'thyme', 'rosemary', 'basil', 'mint', 'parsley', 'chives', 'cilantro',
                'dill', 'vanilla', 'chocolate', 'caramel', 'honey', 'maple', 'sugar', 'salt', 'pepper', 'chili', 'paprika',
                'mustard', 'mayonnaise', 'ketchup', 'soy sauce', 'vinegar', 'olive oil', 'butter', 'cheese', 'yogurt', 'milk',
                'cream', 'egg', 'flour', 'sugar', 'baking soda', 'vanilla extract', 'cocoa', 'coffee', 'tea', 'lemonade']

index=random.randint(0,99)
result=(random_words[index])
length=len(np.unique(list(result)))
# print (length)
print(" _ "*len(result))
# print(result)
answer=""
right=0
wrong=0
lives=10
lose=False
while True:
    print()
    letter=input("input a letter: ")
   
    if letter in result:
        if letter not in answer:
            right+=1
    else:
        wrong+=1
    answer+=letter
    for i in result:
        if i in answer:
            print(i,end=" ")
        else:
            print("_",end=" ")
    print(wrong)
    if(right==length):
        break
    if(wrong==lives):
        lose=True
        break
if(not lose):
    print("Congratulation, You win siuuuuuuuu")
else:
    print("You lose, boooooooooo, the answer is",result)
