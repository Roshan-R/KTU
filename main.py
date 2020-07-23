from clint.textui import progress
import requests

def extract(sem):
    dictionary = {}
    try:
        sources = open("sources/"+sem+".txt","r+")
        source = sources.read()
        for text in source.split('\n'):
            data = text.split('-')
            data = [x for x in data if x]
            if data:
                dictionary[data[0]] = data[1]
        return dictionary
    except:
        if sem.isdigit and int(sem) in range(2,8):
            print("This sem is not supported for now :( ")
            exit()
        else:
            print("Please enter a valid sem number")
            exit()

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
    if num > len(dictionary):
        print("enter a valid number")
        exit()
    else:
        for key,value in dictionary.items():
            if num == nnum:
                download(key,value)
                break
            else:
                nnum += 1

def download(name,url):
    location =  name.replace(' ','_') + '.pdf'
    r = requests.get(url, stream=True)
    with open(location, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

    # os.system("wget -q --show-progress" + url)
    # urllib.request.urlretrieve(url,location)

if  __name__ == "__main__":
    main()
