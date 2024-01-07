def countchar():
    F = open("Beliver.txt","r")
    data=F.read()
    count=len(data)
    print("amount of beliver song characters are", count)
    F.close()
countchar()