# MediBot
An Chatbot based expert system to assist doctors improve screening of patients and diagnosis . 

# Runnable environment
For running the medibot code the following must must be pasted in .bashrc

* export PYTHONPATH="${PYTHONPATH}:/home/path/to/MediBot/bin"
* export PYTHONPATH="${PYTHONPATH}:/home/path/to/MediBot/expert_system"
* export PYTHONPATH="${PYTHONPATH}:/home/path/to/MediBot/lib"



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

#Deliverables on 10 JAN 
* Jaideep : Tokenizers working , JSON accept , LOG (PRINT TOKENS / USERNAME)
* Sameer : Create Medibot , 1_Medibot in telegram , Create listener , pass JSON to Core 

##Functions affected
* Core : core() , make_token , get_user() , read_response() 
* Consumer : TBD 

#Deliverables on 24 JAN 
* Jaideep : convert obo to json , service sample knowledge request , parse knowledge json db , make string input to core pretty
* Sameer : convert / implement non blocking queue based bot producer / consumer , create basic 4 QA db independent EXPERT_SYSTEM 

##Functions affected
* Core :  get_struct()
* Consumer : producer() , consumer()
* Expert_system: (Add functions here sameer)
* knowledge_store:obo_to_json() , service_knowledge_request() , parse_knowledge()


