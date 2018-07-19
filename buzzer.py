
#------------------------import the libraries----------------------------------
import requests #<----- link: http://docs.python-requests.org/en/master/
from bs4 import BeautifulSoup #<---- link: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#---------------------create arrary and int to select arrary items------------
catagory = ['food', 'animals', 'geeky', 'books', 'celebrity', 'community', 'health', 'lgbt', 'music', 'parents', 'politics', 'reader', 'rewind', 'science', 'sports',
'style', 'tech', 'travel', 'weddings', 'world'] #<---- Array of strings used to alter url
catNum = 0 #<---- int used to select array item

#--------------------------------Main fuction of Script---------------------------------
while catNum < len(catagory): #<---- While loop used to control array... select the section on buzzfeed
    i = 10 #<---- int used to determine page number within catagory
    c = str(i) #<---- string version of i for writing url
    while i > 0: #<---- while loop used to control what page we scrape within each section
        r = requests.get("https://www.buzzfeed.com/"+ catagory[catNum] +"?p="+ c +"&z=5I8BVB&r=1") #<---- get web page with url of section catagory[catNum] on page c

        page = r.text #<---- makes web page a text item we can use with Beautiful soup

        soup = BeautifulSoup(page, 'html.parser') #<---- Make Beautiful Soup item out of text page, treated like an html document

        diver = soup.find('div', {'id': 'list-of-buzz'}) #<---- finds the div with id="list-of-buzz" in soup item

        for title in diver.find_all('li'): #<---- loop to find all <li> items in diver item
            print(title.prettify('latin-1')) #<---- print the <li> item on an individual line, then convert it to latin-1 text to avoid encoding errors

        i = i - 1 #<---- change page number
        c = str(i) #<---- reset c to match current value
    catNum = catNum + 1 #<---- move up one item withing catagory array
