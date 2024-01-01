
import urllib.request as urllib

def main(url):
    print("Checking connectivity")
    
    try:
        response = urllib.urlopen(url)
        print(f"Connected to {url} succesfully ")
        print(f"the reponse code was: {response.getcode()}" )
    except:
        print("Ran into Error")

print("Site connectivity Checker ")
url = input("Enter the url of the site you wanna check: ")

main(url)
