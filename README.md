# MediBot
An Chatbot based expert system to assist doctors improve screening of patients and diagnosis . 

# Runnable environment

For maintaining consistency of packages across computers, these steps must be followed:

* Ask Sameer (@v0dro) for the Telegram HTTP API key and load into an environment variable `TELEGRAM_API_KEY` by calling `export` on your command line.
* Install virtualenv with `pip install virtualenv`.
* `cd` into the MediBot directory.
* Activate virtualenv with `source medibot_env/bin/activate`.
* Run whatever code you want.
* New libraries etc MUST be installed through this.

#Date : 2 JAN 2016
## Conventions

* Tabs = Spaces*2 
* Filenames = abc_efg.py
* Verbose logging needed 
* ownership = Funtctional level

##Softwares 
* Anaconda - latest 
* Sublime - defaults 
* Python : 3.x / 2.7 TBD after delebrations , for now 3.4 



##Folders 
* Consumer = Sameer
  -To poll Telegram API and GET JSON dict .
* Core = Jaideep Kekre 
  -To play with JSON dict and display tokenized contents in log / CLI / Return to user as an echo (DEBUG)

##Deliverables on 10 JAN 
* Jaideep : Tokenizers working , JSON accept , LOG (PRINT TOKENS / USERNAME)
* Sameer : Create Medibot , 1_Medibot in telegram , Create listener , pass JSON to Core 
##Functions 
* Core : core() , make_token , get_user() , read_response() 
* Consumer : TBD 


