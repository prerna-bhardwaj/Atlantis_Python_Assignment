import requests
import json


class DictionarySearch:
    """ Returns the meaning of an English language word provided by the user. """
    
    def __init__(self) -> None:
        self.word = ''


    def inputWord(self):
        # Obtain word to be searched
        self.word = input('\nWord ? ')


    def getMeaning(self):
        # Generate URL
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'.format(word=self.word) 
        # Make Get request to API
        response = ''
        # Try except block
        try:
            response = requests.get(url)
            # print(response)

            # If request was made successfully
            if response.status_code == 200:
                content = json.loads(response.content)
                # Obtain list of meanings for given word
                meanings = content[0]['meanings']
                
                print('\nOUTPUT : ')
                # Iterate over all the meanings
                for meaning in meanings:
                    # Print Part of Speech
                    print('\nPART OF SPEECH :', meaning['partOfSpeech'])
                    
                    # Obtains all definitions for a given figure of speech
                    definitions = meaning['definitions']
                    print('DEFINITIONS : ')
                    # Iterate and print all the definitions
                    for index, item in enumerate(definitions):
                        print('  {index}. {defn}'.format(index=index+1, defn=item['definition']))
            
            # In case of unsuccessful request
            elif response.status_code == 404:
                print("We couldn't find definitions for the word you were looking for.")

        # Except block for handling exceptions
        except requests.exceptions.HTTPError as errHttp:
            print(errHttp)
        except requests.exceptions.ConnectionError as errConn:
            print("Unable to connect to the internet. Please check your network connectivity.")
        except requests.exceptions.Timeout as errTime:
            print(errTime)
        except requests.exceptions.RequestException as errReq:
            print(errReq)
        except Exception as e:
            print('Error occured while fetching the data.')



    def runCode(self):
        print('Type -1 to exit')
        # Repeatedly accept words from user
        while True:
            # Accept input
            self.inputWord()
            # If input is -1, break out of the loop
            if self.word == '-1':
                print('Exiting.')
                break
            # Obtain definition of the given word
            self.getMeaning()



# Creating instance of class DictionarySearch
obj = DictionarySearch()
# Repeatedly accept words from user and print their meanings.
obj.runCode()