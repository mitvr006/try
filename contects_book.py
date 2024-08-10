import json
import logging
logging.basicConfig(level=logging.INFO)
try:
    with open ("contects.json","r") as file:
        contects=json.load(file)

except:
   contects={}

while True:
    userchoice=int(input("\nwelcome guys\nchoose what you want to do\n1.Add contect\n2.View contect\n3.Remove contect\n4.exit\nyour choice is:"))

    if userchoice==1:
        while True:
            name=str(input("Enter your name:"))
            phoneno=int(input("Enter your phone number:"))
            email=str(input("Enter your email:"))
            contects[name]={"phone number":phoneno,"email":email}
            choice=str(input("you want to add more number y/n:"))
            if (str.lower(choice)=="n"):
                break
    if userchoice==2:
        while True:
            try:
                n_search=str(input("Enter name to search number:"))
                logging.info(contects[n_search])  
            except:
                logging.error("contect not found\n")
                next=str(input("you went to search another contects y/n:"))
                if (str.lower(next)=="n"):
                         break
    if userchoice==3:
        while True:
            try:
                remove=str(input("Enter name of contect you went to delete:"))
                contects.pop(remove)
                delmore=str(input("you went to search another contect y/n:"))
                if(str.lower(delmore))=="n":
                        logging.info(contects)
                        break
                for k,v in contects.items():
                        logging.info(f"{k}={v}")
            except:
                logging.info("no user found to delete")
                break
    if userchoice==4:
     while True:
           break
 
            
            
                 





              





