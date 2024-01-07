import random
questions=[
    "Suku apa yang menyebarkan bahasa indonesia?",
    "Bonjour artinya?",
    "Who is the most famous French footballer(Soccer Player)?",
    "Bahasa apa yang dipakai di Belgia",
    "The UK has 4 States, mention the name of this?",
    ]
pilihan=[
    [
        "A. Jawa", "B. Minangkabau", "C. Melayu", "D. Papua"
    ],
    [
        "A. Terima kasih", "B. Halo", "C. Selamat Malam", "D. Israel Jahat"
    ],
    [
        "A. Ben Yedder", "B. Dayot Upamecano", "C. Lionel Messi", "D. Kylian Mbappe"
    ],
    [
        "A. Prancis, Belanda dan Jerman", "B. Italia, Inggris, Mandarin", "C. Spanyol, Arab, Urdu", "D. Melayu, Mandarin, Tamil"
    ],
    [
        "A. France, England, Norway, Italy", "B. England, Wales, Scotland, Northern Ireland", "C. Scotland, Ireland, England, Netherlands", "D. Belgium, England, France, Wales"
    ]
]
jawaban= [2,1,3,0,1]
code=["A","B","C","D"]
print("Welcome to quiz game")
Qno= [0,1,2,3,4]
Score=0
random.shuffle(Qno)
# print(Qno)
for i in Qno:
    print()
    print(questions[i])
    for j in pilihan [i]:
        print(j)
    answer=input("jawaban A, B, C, D?")
    # print(answer,code[3],i)
    if(i==1 and answer=="D"):
        Score+=1000
        print("You are Correct, Die Israel go to the hell")
    elif(answer==code[jawaban[i]]):
        Score+=10
        print("You are Correct, lovely")
    else:
        print("You are wrong")
print("Your Score is :",Score)
