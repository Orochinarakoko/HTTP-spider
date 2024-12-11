# HTTP-spider
A python script which can search for directories or files on a website , using the requests module. 


# How to use


- You will need to install the modules "threading" , "queue", and "requests" using pip:
         - Linux/MacOS : Open terminal > type command "python3 -m pip install X"
         - Windows : Open cmd > type command "py -m pip install X"

  

- When the script is run , you will see a menu asking you to select the "mode" you want ( esentially whether you want to check for files, directories or both and in what order
- Then , enter the target URL as promted - to test I used " http://testphp.vulnweb.com "
- Then , enter the desired amount of threads to use - more threads = faster attack, however I RECOMMEND NO MORE THAN 25 OR PACKETS WILL BE DROPPED BY TARGET URL
- Then , enter the name of the wordlist you want to use - it MUST BE IN THE SAME DIRECTORY AS THE PYTHON SCRIPT
- The scipt will carry out the desired scan. After , if you have found any directories , you asked wheter you want to scan found directories for files - enter Y for yes or N for no - YOU WILL NOT BE ABLE TO CARRY OUT THIS SCAN IF YOU HAVE ONLY FOUND FILES
- If you do not want to scan the direcotries , you can enter no , and if you wan to exit the program , you are then asked as to wheter you want to quit - to do so enter "q"
- The script will continue to run untill you prompt it to quit.

  

# Troubleshooting 

If you are recieving "ERROR - CANNOT CONNECT TO ___________ - TRY MANUALLY":
  1) Check you have entered the URL correctly - when using this script this is the most common error I made.
  2) Try reducing the number of threads you are using , GENERALLY TO LESS THAN 25 , as the high request rate may cause requests to be dropped
  3) Try changing the "agent" variable to your own user-agent - this can be found by searching "What is my user agent" in your browser.
  4) Check that your internet connection is up
  5) Check python has the correct permissions to connect to the internet

If you are reciving "ModuleNotFoundError: No module named "X":
  You need to install the module using pip. :
   - Linux/MacOS : Open terminal > type command "python3 -m pip install X"
   - Windows : Open cmd > type command "py -m pip install X"

If you are receiving "
     


# How it works
 - The script goes through a wordlist that the user must provide , and organises it in to the appropriate queues.
 - The script then starts multiple threads , in ord
