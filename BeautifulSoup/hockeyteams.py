'''web scraper that can 
   get all data of NHL teams since 1990
   conduct search and paginate through the results
   get data of a particular page
   site: https://www.scrapethissite.com/pages/forms/'''
   
import requests
from bs4 import BeautifulSoup

#function to parse HTML document into a Python objects
def soup_object(params):
	URL = 'https://www.scrapethissite.com/pages/forms/'
	r = requests.get(URL,params)
	soup = BeautifulSoup(r.text,"lxml")
	return soup

#function to get data of any single page
def page_data(team_data):
	
	for team in team_data:
		column = team.find_all("td")
		
		print("Team Name:",column[0].text.strip())
		print("Year:",column[1].text.strip())
		print("Wins:",column[2].text.strip())
		print("Losses:",column[3].text.strip())
		print("OT Losses:",column[4].text.strip())
		print("Win %:",column[5].text.strip())
		print("Goals For (GF):",column[6].text.strip())
		print("Goals Against (GA):",column[7].text.strip())
		print("+ / -: ",column[8].text.strip())
		print()
	
#function to get all data NHLteams
def all_data():

	#set maximum per_page for reducing number of request
	soup = soup_object({"per_page":100})
	pagination = soup.find("ul",class_="pagination")
	no_of_pages = pagination.find_all("li")
	
	#iterate through all pages
	for pages in no_of_pages:
		soup = soup_object({"page_num":pages.a.text,"per_page":100})
		team_data = soup.find_all("tr",class_="team")
		page_data(team_data)
		
		
#function to get data of a particular team
def search_team():

	search = input("Search team")
	soup = soup_object({"q":search})
	pagination = soup.find("ul",class_="pagination")
	no_of_pages = pagination.find_all("li")
	
	#checking for more than one page
	if no_of_pages != []:
		for pages in no_of_pages:
			soup = soup_object({"page_num":pages.a.text,"per_page":100})
			team_data = soup.find_all("tr",class_="team")
			
			if team_data != []:
				page_data(team_data)
			else:
				print("Data not found")
				break
	else:
		team_data = soup.find_all("tr",class_="team")
		
		#checking if team exist or not 
		if team_data != []:
			page_data(team_data)
		else:
			print("Data not found")

#function to get data of a particular page
def data_per_page():

	per_page = input("Enter number of data per page options are 25|50|100")	
	#checking for valid data per page
	if per_page != '25' and per_page != '50' and per_page != '100':
		print("Invalid data per page entry")
		
	else:
		print("6 pages for 100 data per page")
		print("12 pages for 50 data per page")
		print("24 pages for 25 data per page")
		page_number = input("Enter page number")
		
		soup = soup_object({"page_num":page_number,"per_page":per_page})
		team_data = soup.find_all("tr",class_="team")
			
		#checking if that page exist or not
		if team_data != []:
			page_data(team_data)
		else:
			print("Invalid page number")
			

		
if __name__ == "__main__":
	
	#menu of operations
	while True:
	
		print("Database of NHL team stats since 1990")
		choice = input('''Enter   1 for get all data
      	2 for get data of specified team
      	3 for get data from particular page
      	4 for exit''')
      	
		if choice == '1':
			all_data()
		elif choice == '2':
			search_team()
		elif choice == '3':
			data_per_page()
		elif choice == '4':
			break
		else:
			print("Invalid choice")
		print()
	'''web scraper that can 
   get all data of NHL teams since 1990
   conduct search and paginate through the results
   get data of a particular page
   site: https://www.scrapethissite.com/pages/forms/'''
   
import requests
from bs4 import BeautifulSoup

#function to parse HTML document into a Python objects
def soup_object(params):
	URL = 'https://www.scrapethissite.com/pages/forms/'
	r = requests.get(URL,params)
	soup = BeautifulSoup(r.text,"lxml")
	return soup

#function to get data of any single page
def page_data(team_data):
	
	for team in team_data:
		column = team.find_all("td")
		
		print("Team Name:",column[0].text.strip())
		print("Year:",column[1].text.strip())
		print("Wins:",column[2].text.strip())
		print("Losses:",column[3].text.strip())
		print("OT Losses:",column[4].text.strip())
		print("Win %:",column[5].text.strip())
		print("Goals For (GF):",column[6].text.strip())
		print("Goals Against (GA):",column[7].text.strip())
		print("+ / -: ",column[8].text.strip())
		print()
	
#function to get all data NHLteams
def all_data():

	#set maximum per_page for reducing number of request
	soup = soup_object({"per_page":100})
	pagination = soup.find("ul",class_="pagination")
	no_of_pages = pagination.find_all("li")
	
	#iterate through all pages
	for pages in no_of_pages:
		soup = soup_object({"page_num":pages.a.text,"per_page":100})
		team_data = soup.find_all("tr",class_="team")
		page_data(team_data)
		
		
#function to get data of a particular team
def search_team():

	search = input("Search team")
	soup = soup_object({"q":search})
	pagination = soup.find("ul",class_="pagination")
	no_of_pages = pagination.find_all("li")
	
	#checking for more than one page
	if no_of_pages != []:
		for pages in no_of_pages:
			soup = soup_object({"page_num":pages.a.text,"per_page":100})
			team_data = soup.find_all("tr",class_="team")
			
			if team_data != []:
				page_data(team_data)
			else:
				print("Data not found")
				break
	else:
		team_data = soup.find_all("tr",class_="team")
		
		#checking if team exist or not 
		if team_data != []:
			page_data(team_data)
		else:
			print("Data not found")

#function to get data of a particular page
def data_per_page():

	per_page = input("Enter number of data per page options are 25|50|100")	
	#checking for valid data per page
	if per_page != '25' and per_page != '50' and per_page != '100':
		print("Invalid data per page entry")
		
	else:
		print("6 pages for 100 data per page")
		print("12 pages for 50 data per page")
		print("24 pages for 25 data per page")
		page_number = input("Enter page number")
		
		soup = soup_object({"page_num":page_number,"per_page":per_page})
		team_data = soup.find_all("tr",class_="team")
			
		#checking if that page exist or not
		if team_data != []:
			page_data(team_data)
		else:
			print("Invalid page number")
			

		
if __name__ == "__main__":
	
	#menu of operations
	while True:
	
		print("Database of NHL team stats since 1990")
		choice = input('''Enter   1 for get all data
      	2 for get data of specified team
      	3 for get data from particular page
      	4 for exit''')
      	
		if choice == '1':
			all_data()
		elif choice == '2':
			search_team()
		elif choice == '3':
			data_per_page()
		elif choice == '4':
			break
		else:
			print("Invalid choice")
		print()
	
