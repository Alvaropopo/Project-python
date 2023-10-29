import random

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
print(" _ "*len(result))
# print(result)
answer=""
right=0
while(right>=len(result)):
    print()
    letter=input("input a letter: ")
    answer+=letter
    
    wrong=0
    for i in result:
        if i in answer:
            print(i,end=" ")
            right+=1
        else:
            print("_",end=" ")
            wrong=1
    print(answer)

