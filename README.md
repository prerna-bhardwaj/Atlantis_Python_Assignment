# Atlantis Python Assignment

## Setup

The `requirements.txt` file contains the list all Python libraries required to run the project.
Install the modules using the following command :

```
pip install -r requirements.txt
```

To run a code file named code.py run the following command: 

```
python code.py
```

You are good to go !!


## Assessment Questions

Following is the list of Assignments implemented in python. 
Links to the code files have been attached : 

### Assignment 1: Saved in [search_repos.py](https://github.com/prerna-bhardwaj/Atlantis_Python_Assignment/blob/master/search_repos.py)
Write a python program to scrape the list of links available in this Github repository (https://github.com/vinta/awesome-python) and search them by exact name from the console. Search result should return the github url of the result repository. 

Expected output: 

> $ python search_repos.py<br>
> Query? graphene <br>
> Output: https://github.com/graphql-python/graphene/

The list should be scraped and kept in a runtime variable as soon as the program is initialized.. Handle the error with a suitable error message in case the exact name is not matched from the list. 


### Assignment 2: Saved in [dictionary_search.py](https://github.com/prerna-bhardwaj/Atlantis_Python_Assignment/blob/master/dictionary_search.py)
Write a python class that is able to return the meaning of an English language word provided to it in the terminal. (Use https://dictionaryapi.dev/) 

Expected output:
> $ python dictionary_search.py<br>
> Word? <user inputs the word “House”><br>
> Output: House. Noun. A building for human habitation, especially one that is lived in by a family or small group of people. 


### Assignment 3: Saved in [city_distance.py](https://github.com/prerna-bhardwaj/Atlantis_Python_Assignment/blob/master/city_distance.py)
Write a python class that is able to return the flight distance between two cities given their latitude and longitude coordinates. 

Expected output: 
> $ python city_distance.py<br>
> City 1: 51.5074 N, 0.1278 W<br>
> City 2: 48.8566 N, 2.3522 E<br>
> Output: City 1 and City 2 are 342.87 km apart

### Assignment 4: Saved in [wifi.py](https://github.com/prerna-bhardwaj/Atlantis_Python_Assignment/blob/master/wifi.py)
Write a python class that is able to find three available WiFi networks with the strongest signal and connect to the one where the password is provided. 

Expected output: 
> $ python wifi.py<br>
> Your available wifi networks are: <br>
> [1] Wifi_network 1<br>
> [2] Wifi_network 2<br>
> [3] Wifi_network 3<br>
> Your choice? 3<br>
> Password: *******<br>
> connected!

***NOTE : Assignment 4 works only on Linux Systems.***
