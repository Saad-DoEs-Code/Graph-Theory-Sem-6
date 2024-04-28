import requests
from bs4 import BeautifulSoup


with open(file="tags.html",mode= 'r') as f:
    html_doc = f.read()

soup= BeautifulSoup(html_doc, 'lxml')

#  Getting full document
# print(soup.prettify())

# Getting Tags
print(soup.h1.text)
# Getting All <p> Tags
print(soup.find_all('p'))
# Getting Name of Tag
print(soup.title.name)

# Getting Text of <li> Tag 
for li in soup.find_all('li'):
    print(li.text)

#  Getting All <a> Tags and its href
# for a in soup.find_all('a'):
#     print(a.get('href'))

# Get first <a> Tag of the HTML Document and return its href
s = soup.find('a')
print(s.get('href'))


# Getting Text by ID
print(soup.find(id='content').text)


# Getting Div by Class
print(soup.select('div.italic'))
# Getting Div by ID
print(soup.select('span#italic-span')[0].text)
#  Getting whole Class List of a Tag
print(soup.span.get('class'))

#  Finding with the help of ID/Class
print(soup.find_all(class_='italic')[0].text)
print(soup.find_all(id='italic-span')[0].text)

#  Finding Cildren inside a Class
for child in soup.find     (class_='container').children:
    print(child.text)


# Modifying a Tag
tag = soup.find(class_="container")
tag.name= "section"
tag.string= "This is a new modified section" # It will change the inner content 
tag["class"]= ["container-fluid", "bg-dark"]
tag["id"] = "container-id"
tag["style"] = "color: white; background-color: black"
print(tag)


# Inserting New Tags
# Step 1. Create a new Tag
new_ul_tag= soup.new_tag("ul")
# Step 2. Insert the new Tag inside the existing Tag
li_tag=soup.new_tag('li')
# Step 3. Giving li Tag, some text
li_tag.string= "Home"
new_ul_tag.append(li_tag)
li_tag= soup.new_tag('li')
li_tag.string= "About"
new_ul_tag.append(li_tag)

soup.body.insert(0, new_ul_tag)

with open("New-HTML.html", "w") as f:
    f.write(str(soup))

# Finding if an Attribute is present or not
cont= soup.find(id="this-cont")
print(cont.has_attr("contenteditable"))

def has_class_and_not_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

results= soup.find_all(has_class_and_not_id)
for result in results:
    print(result.name)
    print(result.get('class'))


