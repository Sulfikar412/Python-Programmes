f=open("demo.txt","r")
count=0

for word in f.read().split():
    if len(word)==4:
        count+=1
        
print("count of four letter words :",count)
