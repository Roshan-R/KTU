import urllib.request

def extract(sem):
    dictionary = {}
    try:
        sources = open(sem+".txt","r+")
        source = sources.read()
        for text in source.split('\n'):
            data = text.split('-')
            data = [x for x in data if x]
            if data:
                dictionary[data[0]] = data[1]
        return dictionary
    except:
        print("There is no file like this")
        main()

def main():      
    print("Welcome to the KTU python asssist tool!")
    sem = input("Enter your sem : ")
    print()
    if sem != 'x':
        dictionary = extract(sem)
        x = 1
        for key in dictionary.keys():
             print('{:3}'.format(str(x)),' : ',key)
             x += 1
        num = int(input("\nEnter the number : "))
    nnum = 1
    for key,value in dictionary.items():
        if num == nnum:
            download(key,value)
            break
        else:
            nnum += 1

def download(name,url):
    location =  name.replace(' ','_') + '.pdf'
    urllib.request.urlretrieve(url,location)

if  __name__ == "__main__":
    main()