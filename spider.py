##########################################################################################
# AUTHOR: James Chacksfield                                                              #
# NAME : HTTP SPIDER.py                                                                  #
# DESCRIPTION : Program uses a wordlist to send HTTP requests to a passed url - if the   #
#               HTTP response code is 200 , the direcotry / file must exist              #
#                                                                                        #
#                                                                                        #
# I do not condone the use of this program for unauthorised , illegal activity. Using    #
# this program without the permission of the target IS A CRIME , which may lead to fines #
# or jail time                                                                           #
##########################################################################################


#-----------------------------------------------------------------------------------------
import time
import threading
import requests
import queue
import sys
#-----------------------------------------------------------------------------------------

wordlist = []

dirlist = queue.Queue()

existingdirs = []

filelist = queue.Queue()

dirfilelist = queue.Queue()

threads = []

#-----------------------------------------------------------------------------------------

agent = ("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0")




headers = {"user agent" : agent}

#-----------------------------------------------------------------------------------------

def make_wordlist(filename):

    try:

        file = open(filename,"r")

    except FileNotFoundError:
        print(f"No file in this directory called {filename}")
        sys.exit()

        
    except:
        print(f"Error opening {filename} - is it password protected?")
        sys.exit()
   
    for line in file:
   

        line = line.strip()

           
        if "." in line:
            filelist.put(f"/{line}")
            wordlist.append(f"{line}")
        else:
            dirlist.put(f"/{line}/")





#-----------------------------------------------------------------------------------------
           

def phase1(url):



#---------------------------------------------------------- Scan for directories
   
    while not dirlist.empty():

        try:

            i = dirlist.get()
       

            r = requests.get(f"{url}{i}" , headers = headers)

            if r.status_code == 200:
                print(f" 200 SUCCESS : {url}{i}")

                existingdirs.append(i)

            else:
                continue

        except:
            print(f"ERROR - CANNOT CONNECT TO {url}{i} - TRY MANUALLY")



#--------------------------------------------------------- Scan  for files in / directory

def phase2(url):

    while not filelist.empty():
       
        i = filelist.get()


        try:
       
            r = requests.get(f"{url}{i}",headers = headers)
        except:
            print(f"ERROR - CANNOT CONNECT TO {url}{i} - TRY MANUALLY")


        if r.status_code == 200:
            print(f" 200 SUCCESS : {url}{i}")

        else:
            continue







#------------------------------------------------------------------------------------- Scan directories that have already been found

def phase3():

    for i in existingdirs:
        for j in wordlist:
            dirfilelist.put(f"{i}{j}")



def phase4(url):

    while not dirfilelist.empty():

        i = dirfilelist.get()

        try:
            r = requests.get(f"{url}{i}" , headers = headers)
        except:
            print(f"ERROR - CANNOT CONNECT TO {url}{i} - TRY MANUALLY")

           

        if r.status_code == 200:
            print(f" 200 SUCCESS : {url}{i}")

        else:
            continue

#------------------------------------------------------------------------------------- Get URL from user

def get_info():


    print(""" SELECT MODE :
1 - Directories only
2 - Files only
3 - Directories then Files
4 - Files then Directories
5 - Quit""")

    while True:

        try:

            userMode = int(input(">>> "))


            if userMode > 5 or userMode < 1:
                print("Invalid Input")
               
            else:
                break

        except:
            print("Invalid Input")


    if userMode == 5:
        print("Goodbye")
        sys.exit()


       


       
    while True:
       
        print("Enter URL")

        try:

            url = str(input(">>> "))

            if url[-1] == "/":
                url = url[0:-1]

            break

        except:
            print("Invalid Input")



    while True:

        print("How many threads do you want to spawn?")


        try:

            numThreads = int(input(">>> "))
            break

        except:
            print("Invalid Input")


    while True:
        print("Enter wordlist name : ")
        try:
            filename = str(input(">>> "))
           
            if ".txt" not in filename:
                filename = filename + ".txt"


           
            break
        except:
            print("Invalid input")
           
           
           


    return url , numThreads , userMode , filename

#----------------------------------------------------------------------------------- Run the defined functions , looping untill the user quits


while True:        

    url , numthreads , phase ,filename = get_info()

    make_wordlist(filename)
       
    if phase == 1:
       
        print("")
        print("DIRECTORIES")
        print("")
       
        for i in range(numthreads):
            t = threading.Thread(target = phase1 , args = (url,))
            t.start()

        while True:
            if dirlist.empty():
                break
            else:
                continue

    elif phase == 2:
       
        print("")
        print("FILES")
        print("")
       
        for i in range(numthreads):
            t = threading.Thread(target = phase2 , args = (url,))
            t.start()

        while True:
            if filelist.empty():
                break
            else:
                continue

    elif phase == 3:
        print("")
        print("DIRECTORIES")
        print("")
        for i in range(numthreads):
            t = threading.Thread(target = phase1 , args = (url,))
            t.start()

        while True:
            if dirlist.empty():
                break
            else:
                continue

        print("")
        print("FILES")
        print("")

        for i in range(numthreads):    
            t = threading.Thread(target = phase2 , args = (url,))
            t.start()

        while True:
            if filelist.empty():
                break
            else:
                continue


                   
    elif phase == 4:
        print("")
        print("FILES")
        print("")
        for i in range(numthreads):
            t = threading.Thread(target = phase2 , args = (url,))
            t.start()


        while True:
            if filelist.empty():
                break
            else:
                continue

           


        print("")
        print("DIRECTORIES")
        print("")

       
                       
        for i in range(numthreads):
            t = threading.Thread(target = phase1 , args = (url,))
            t.start()


        while True:
            if dirlist.empty():
                break
            else:
                continue

           




    if dirlist.empty():

        print("")



        while True:

           

           
            print(" Do you want to scan found directories for files ? (Y/N) ")

            q = str(input(">>> "))



            if q.upper() == "Y" or q.upper() == "YES":
                phase3()
                for i in range(numthreads):
                    t = threading.Thread(target = phase4 , args = (url,))
                    t.start()

                break

            elif q.upper() == "N" or q.upper() == "NO":
                break

            else:
                print("Invalid Input ")


        while True:
            if dirfilelist.empty():
                break
            else:
                continue
               
           

        print("")
        print("Press any key to continue , or Q to exit:")

        furtherscans = str(input(">>> "))

        if furtherscans.upper() == "Q":
            sys.exit()

        else:
            continue

    else:
        print("")
        print("Press any key to continue , or Q to exit:")

        furtherscans = str(input(">>> "))

        if furtherscans.upper() == "Q":
            sys.exit()

        else:
            continue
