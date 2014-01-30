# Interactions Task	

### Background and Purpose
The research team responsible for the pilot are collecting various types of production related quantitative data covering inputs (yarn, labour, capital) and output (including quality defects etc.). The aim of doing so is to try to pinpoint any increases in productivity during the life of the project. The Interactions task is needed in order to pinpoint what role communication between a team supervisor and his subordinates and other in the factory has to play in any observed changes in productivity. 

<br />
### Measuring Interactions
The basic idea is to measure the interactions that occur between the supervisor that supervises each of the knitting/linking teams that are being observed. The observed (and hence the user of the application) will follow a supervisor for a predefined amount of time each day (currently thought to be one hour per team) and observe and record the interactions that occur in that period. 

The interactions that are of interest are as follows:
+ Supervisor to Operator from own team
+ Supervisor to Operator from another team
+ Supervisor to Supervisor from another team
+ Supervisor to Floor in Charge
+ Supervisor to Production Management
+ Supervisor to Other Management
+ Supervisor to Unknown 

Additionally the observer will record a null interaction which has the following interpretation:
+ Supervisor left floor (unable to follow)

The data that are to be gathered for each of the above interactions (save the null observation) is as follows:

1. Duration  - duration of the interaction in seconds.

2. Initiator - who initiated the interaction, a coded response:
	+ 1 = 'Supervisor'
	+ 2 = 'Interlocutor'
	+ 3 = 'Unclear'

3. Topic - the topic of the interaction, a coded response:
 	+ 1 = 'Related to machine configuration'
	+ 2 = 'Related to machine function'
	+ 3 = 'Related to yarn'
	+ 4 = 'Related to pattern'
	+ 5 = 'Other work related'
	+ 6 = 'Personal'

**NB** The above typologies are not yet ascertained. 

It appears currently that when coding using console.input_alert() only 3 options are allowed. This will have to be overcome for data points that have more than 3 reponse options as above. 
	
<br />
###Data Structures
In addition to the machine codes (KN1, LI1 etc.) the following codes will be defined to represent the other types of interaction:

+ 'OO'  -  other operator
+ 'OS'  -  other supervisor
+ 'FIC' -  floor in charge
+ 'PM'  -  production management
+ 'OM'  -  other management
+ 'O'   -  other
	
At present I suspect it would be easier in terms of the readability of the code to produce this to have one interaction object (dict) created for each interaction as it is observed, but at the end of the task before the data are saved to dropbox for that data to automatically be placed in a daily interactions task level dictionary that will then be saved as a json. The individual interaction dictionary would look as follows (with an interaction with the floor in charge):

		Interaction1 = { 'interaction_id' : 'FIC', 'interaction_length' : 55,  'initiator' : 1, topic : 3}
		Interaction2 = { 'interaction_id' : 'KN1', 'interaction_length' : 132, 'initiator' : 2, topic : 4}

	
Separately a list item could be created that measures the amount of time the supervisor was absent without the observer being able to follow. The elements of this list would be the number of seconds of each time that supervisor left the floor and the observer was unable to follow.
	
At the end of the hour during which the task is created, all of the dictionaries created could be compiled into a single dict to be stored as json. I hold off displaying the format of this for now as it remains unclear to me as to whether the order of the interactions should be preserved, or whether some cumulative measure would suffice.


###User Interface
The console is probably sufficient for the wip task, however it is manifestly insufficient for the interactions task. Ideally when configuring the application the user will be asked to place as many buttons (referenced by the machine code) as there are machines to be followed according to some grid that represents some semblance of reality. When the interaction task is begun these buttons can form the UI, coloured white if the associated id_dict entry has 'manned' for mc_status, and dark grey if the machine 'Unmanned' as per the id_dcit. Additional buttons for the other interactions should be present for the interactions task, as well as a button which will allow the user to state that the supervisor has left the floor.

The user may cancel if the wrong button is chosen to prevent accidental erroneous data being from being collected. [However, possibly once the routine is entered for each interaction beyond the first touch the user will be unable to cancel.

A sketch of one possible look for the interface is as follows:

![alt text](http://programtheworld.files.wordpress.com/2014/01/interactions_gui_template.png "UI Template Draft")  