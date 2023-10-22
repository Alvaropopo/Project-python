import random


def test_ielts():
    return random.uniform(3,5.7)
target_ielts= 5.5
hasil_ielts= 3
counter=0
nama=input("masukan nama: ")
while(hasil_ielts<target_ielts):
    counter+=1
    print(counter,".",nama,":nilai ieltsmu", hasil_ielts,"kamu harus mencoba kembali")
    hasil_ielts=test_ielts()

print("nilai ieltsmu", hasil_ielts,"kamu mencapai target")