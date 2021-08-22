# Importing required modules 
import subprocess
import getpass


class ConnectToWifi:
    """ Finds 3 available WiFi networks with the strongest signal and connects to the one
        for which a password is provided. """


    def __init__(self) -> None:
        # List for storing the top 3 networks
        self.networks = []

    
    def getNetworkData(self):
        # getting data of wifi networks
        output = subprocess.check_output("nmcli -f ssid dev wifi", shell=True)
        # decoding the data
        output = output.decode('utf-8')

        # splitting the data line by line
        wifi = output.split('\n')
        for line in wifi[1:4]:
            try:
                if line != '':
                    self.networks.append(line.strip())
            # Print error message in case there are < 3 networks
            except IndexError as e:
                print('3 networks are not available.\n')


    def printTop3Networks(self):
        # Print the top 3 networks
        for index, nw in enumerate(self.networks):
            print('[{index}] {network}'
                    .format(index=index+1, network=nw))


    def connectToNetwork(self):
        # Try Except Block
        try:
            # Accept network choice and password from user
            choice = int(input('Your choice? '))
            password = getpass.getpass("Password: ")
            # Obtain name of chosen network from networks list.
            currNw = "'" + self.networks[choice-1] + "'"
            
            # Command for connecting to network using password
            command = 'nmcli dev wifi connect {network} password "{password}"'.format(network=currNw, password=password)
            output = subprocess.check_output(command,shell=True, timeout=30)
            output = output.decode('utf-8')
            
            # In case of error, raise an exception
            if output.find('Err') != -1:
                raise Exception("Unable to connect to chosen network. Please try again later.")
            # Connection has been established successfully
            else:
                print('Connected !')
        except ValueError as e:
            # When user enters non-integer value for choice
            print('Please enter an Integer value')
        except IndexError as e:
            # When choice is < 1 or greater than # of available networks
            print('Please enter a valid choice.')
        except subprocess.CalledProcessError as e:
            print('Please check you password once again.')
        except subprocess.TimeoutExpired as e:
            print('Network took too long to connect.')
        except Exception as e:
            print("Error : ", e)


# Create instance of ConnectToWifi class
wifi = ConnectToWifi()
# Obtain meta data of available networks
wifi.getNetworkData()
# Print top 3 networks with the strongest signal
wifi.printTop3Networks()
# Connect to a chosen network
wifi.connectToNetwork()