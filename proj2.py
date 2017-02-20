#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")


count = 0
for story_heading in soup.find_all(class_="story-heading"):
	if count < 10:	
		if story_heading.a:
			print(story_heading.a.text.replace("\n", " ").strip())
		else:
			print(story_heading.contents[0].strip())
		count += 1
	else:
		break

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'https://www.michigandaily.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
most_reading = soup.find_all(class_="pane-mostread")
for item in most_reading:
	for i in item.descendants:
		if i.name == 'a':
			print (i.contents[0].strip())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
tag_img = soup.find_all('img')
for item in tag_img:
	try:
		print (item['alt'])
	except:
		print ('No alternative text provided!')



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
r = requests.get(base_url,headers={'User-Agent': 'SI_CLASS'})
soup = BeautifulSoup(r.text, "html.parser")
current_page = (soup.find_all(class_='pager-current'))[0].contents
print (current_page)

count = 1
flag = True
while flag:

	flag = False
	if int(current_page[0][0]) <= int(current_page[0][-1]):
###################  Extract Email-address from one page  ###################################
		contact_link = soup.find_all('a')
		for i in contact_link:
			if i.string == 'Contact Details':
				contact_url = 'https://www.si.umich.edu' + i['href']
				contact_r = requests.get(contact_url,headers={'User-Agent': 'SI_CLASS'})
				soup = BeautifulSoup(contact_r.text, "html.parser")
				email_ls = soup.find_all('a')
				for i in email_ls:
					if '@umich.edu' in i.contents[0]:
						print ("{} {}".format(count, i.contents[0]))
						count += 1
################### Move to next page  ######################################################
			if i.string == 'next ›':
				page_link = i['href']
				page_url ='https://www.si.umich.edu'+ page_link
				r = requests.get(page_url,headers={'User-Agent': 'SI_CLASS'})
				soup = BeautifulSoup(r.text, "html.parser")
				current_page = (soup.find_all(class_='pager-current'))[0].contents
				flag = True

	else:
		flag = False


















