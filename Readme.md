|     |     |
| --- | --- |
| Application: | **RMG-Observations** |
| Author:      | **Rory Creedon** (rcreedon@poverty-action.org) |
| Use:         | **Intended for deployment on iPad through Pythonista application** |

Purpose of the application is to allow the user to make observations of work in progress (WIP) in a sweater factory.

**Background:** Sweater factories are divided into many different sections. There are two that are of interest for the purpose at hand:

1. **Knitting** - The operators in the knitting section weave yarn into the panels that make up a sweater. Each sweater is comprised of four separate panels. Once all four panels are complete, one piece has been completed. Knitting operators work in batches of 12, that is they receive sufficient yarn to make 12 complete pieces and do not hand over their output until a complete 'bundle' 12 pieces is complete.

    Occasionally they may hand in more than one bundle.
    
    In general there are 30 knitting operators in a team, and they will have one direct supervisor.

2. **Linking** - The operators in the linking section take the completed bundles from the knitting section and link (i.e. sew) the panels together to form a sweater. As with the knitters they work with bundles of 12. They are geographically distinct from the knitters (different floor).

    In general there are 32 linking operators in a team and they will have one direct supervisor.
	
Within each of those sections, the observer will make observations relating to one 'team' of workers. This team is a team that is receiving training as part of a consultancy program and the observations are being made to try to understand how that training affects the way the line works. It is a complex process of measurement of which this application forms only a part. In addition a huge volume of production and HR data will be collected, and various other types of survey work will be undertaken. 

Note that at present it is thought that only one team will be followed in each section. This is the team just described, the 'treatment' team. However, it seems possible that this will be expanded to include a 'control' team as well. 
	
For both Knitting and Linking sections it may prove most useful to think in terms of machines rather than people. This is because the physical space that will be observed will not change, but the operators working in that space may well change. Thus it is unlikely that the machines within the 'team' space will move or change locations (they are large machines, and do not move frequently) whereas the people working those machines may well change either becasue operators leave their work and others replace them, or (unlikely) operators are shifted to different locations within the team)

The factory separately provide the project with data on the individuals that work in the factory which includes attendance and other information about the worker. This data will include the worker ID number as given by the factory. Therefore, if the user is prompted once a day to enter the worker ID numbers of those people he finds working on the line, then this information can be matched with the data provided by the factory. In the program therefore, all references to worker codes should be understood rather as machine codes [perhaps edit the code to make more intuitive]        

In the factories under observation, the observer (i.e. the user of this application) will be present daily, and they will follow a strict diary of the tasks that need to be completed. The tasks will always relate to the same group of knitting/linking operators throughout the duration of the project. Therefore, upon first opening the application, the numbers to be followed, and their ID codes etc need to be determined/input

The observations are strictly controlled i.e. should not provide flexibility to the user as to what data are entered once a task is begun. If a task is begun then it must be completed for every operator for which there is an id code. If a data point is not reuqired for an opeartor under observation, then a null value should be entered and it should be clear from the data structure as to why that data point was not required.

At present the project is in a pilot phase which means that the application will be used in one factory, by one observer. However, conditional on funding and the success of the pilot, this project will be rolled out to around 25 factories with multiple observers. 


**Tasks:** Currently two tasks are contemplated although the application has a lot of potential to be expanded. at present the application should be written such that future tasks can be added:

1. **Measuring WIP** - at one point during the day (late afternoon), the user must record the amount of work in progress. Workers may 'hand in' up to 48 pieces at a time in multiples of 12. The receipt of these bundles of 12 is recorded elsewhere. However, as 12/24/36/48 pieces can take some days to complete recording the number of pieces as work in progress (meaning not yet handed in) is critical to understanding how productive a worker is on a day to day basis. WIP is measured in increments of 0.25.

    For the sake of clarity note that WIP is the number of pieces completed but not handed in.

2. **Recording Interactions** - the scope of this task is not yet fully defined. The basic idea is that for a fixed amount of time the observer will follow a supervisor and record the interaction that he has with the knitting operators. 

**Output:** There are two levels of output currently envisaged: Top Level Ouput and Task Level Output.

The Top Level Output is a dictionary saved as a .json of the following format:

    TopLevelDict = { 'Knitters' : [],
                     'Linkers'  : [] }

This output will be created upon first opening (user configuring) the application.

The Task Level Output will vary by task, although data will be stored in dictionaries and saved a .json files:

* Measuring WIP (example given in the knitting section with machine id code KN1, KN2 etc.:

    WIPDict = { 'DateTime' : '01/14/2014 14:36',
                'KN1'      : { 'mc_status'  : 'Manned',
                               'Style'      : 7,
                               'WIP'        : 4.25 },
                'KN2       : { 'mc_status'  : 'Unmanned',
                               'Style'      : 'null',
                               'WIP'        : 'null'}
              }

**NB** The mc_status variable will be determined by the worker_id routine that should also be completed by the user. For more information about this routine see the 'Other Functionality' section (below)

Initially it was thought by RC that one such file would maintained throughout the project in which the application will be used. However, upon suggestions from contributors this now seems to be the wrong way to go about it. Rather, one dictionary will be created per task and will be saved with a timestamp and task name. 

Similar output should be generated for all tasks implemented in this application.

**Other Functionality:** The application will perform a variety of other functions. At present these are thought to include:

1. **Entering Operator ID Numbers** - Conceptually the observations are at the machine level. Therefore each day the first thing the user should do is for each section to enter the worker ID numbers as given by the factory for each machine that is part of the team being observed.

	The data that this process will generate will take the following format:

		Knitting_IDs = {	'Date' : '01/14/2014',
							'KN1'  : { 'mc_status' : 'Manned',
									   'worker_id' : 'foo'}
							'KN2   : { 'mc_status' : 'Unmanned,
									   'worker_id' : 'null'}}

	This data will be saved to .json. There will one such file created per day for the Knitting section, and one for the Linking section. This process will be completed upon the user first opening the application which will allow the data to be shared across all the task that need to be completed.

	This process will supersede the need for the user to comment on the Attendance of each operator during the tasks.

	One potential issue is that when the process is first undertaken during the morning and the data is stored a machine may be 'unmanned' (i.e. operator did not show) but by the time that a task is undertaken that operator has arrive (i.e. he was late). The task will have to have a routine that allows the user to modify whether the machine is manned or not. 

	conceptually this routine could be thought of as a 'task'. However it is not included in the task list, as the user will not have an option to complete it. It must be completed before any tasks can be undertaken, such that the data the worker id function creates can be shared between tasks. 

2. **Syncing to dropbox** - All data will be synched to drop box

3. **Verifying Observer Presence** - It may seem draconian but it is important that the project manager can monitor the observer to check that he is in fact in the factory making the observations. The factory is geographically remote from the head office, and the project manager will rarely be in the field. Ideally this would be achieved with GPS coordinates, however due to limited 3G coverage and no wireless networks in factories, this will not be. The current solution is that the user will be prompted to take a photo at the end of each task. The photo will be saved with a timestamp and the task name, and the user will have to take the photo such that it can be clearly demonstrated that he is actually at the factory (i.e in front of one of the machines)


