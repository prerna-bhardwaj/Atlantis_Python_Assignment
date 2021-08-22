import requests
from bs4 import BeautifulSoup


class SearchRepos:
    """ Scrape the list of links available in the Github repository : https://github.com/vinta/awesome-python.
        Search them by exact name from the console. Search result is the github url of the result repo. """


    def __init__(self) -> None:
        self.query = ''
        # Url of the github repo to be scraped
        self.base_url = 'https://github.com/vinta/awesome-python'
        # Save words and links scraped in a dictionary
        self.link_data = {}
        """
            link_data = {'graphene' : 'https://github.com/graphql-python/graphene/',
                        'python-patterns' : 'https://github.com/faif/python-patterns'
                    }
        """

    def inputQuery(self):
        # Obtain query to be searched
        self.query = input('\nQuery : ').strip()


    # Scrape and save all links from base url
    def scrapeData(self):
        # Making get request to given url
        response = requests.get(self.base_url)
        # Parse content of page obtained using BeautifulSoup 
        content = BeautifulSoup(response.content, 'html.parser')

        # Obtain division from html page that contains all links
        body = content.find('div', attrs={'class': 'Box-body'})
        print()

        # Obtain list of all links
        links = body.find_all('a')
        print('Total Links Found : ', len(links))

        # Iterate over all links
        for ele in links:
            # Only if the link is ab url to a repo, add its text and link to the link_data dictionary 
            if ele['href'].find('https://') != -1 or ele['href'].find('http://')!=-1:
                self.link_data[ele.text] = ele['href']

        # Print count of total links scraped
        print('Links Scraped : ', len(self.link_data))


    # Obtain link(if present) for a given query.
    def getLink(self):
        link = self.link_data.get(self.query, 'Value not found')
        print(link)        


    # Repeated search links for obtained queries
    def searchQueries(self):
        print('Type -1 to exit.')
        while True:
            self.inputQuery()
            # Break the loop if user entered -1
            if self.query == '-1':
                print('Exiting.')
                break
            # Obtain link for query accepted
            self.getLink()


# Create instance of class SearchRepos
obj = SearchRepos()
# Scrape data and save in link_data dictionary
obj.scrapeData()
# Repeatedly search for queries
obj.searchQueries()