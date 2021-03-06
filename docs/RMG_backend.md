# Ready-Made Garments Backend Strategy

## A backend process will need to gather new observations, integrate them with previous observations, store, backup, and report on observations

###Gather New Observations
Observations will be posted to Dropbox by Observers on a periodic basis. The internet connection in the factories is patchy to non-existent, so updates will happen periodically. There is some question as to whether these updates will happen automatically (?) or whether they will happen upon user request. For more information see Dropbox_sync.md

###Integrate with New Observations into Previous Observations
I have never designed a system like this before. We use pandas for our data work and so given that I understand the pandas objects it would seem to me sensible to use that library for integrating the observations. I would imagine the steps to be something along the lines of the following:
1. Create and store and empty data frames to be populated. There would one data frame per task/department/team. Therefore if the observer follows a treatment and control team in the knitting and linking sections, and there are two tasks (wip and interactions), then there will be 8 data frames. The fields (columns) of the data frames should correspond to fields (keys) of the dictionaries generated byt the tasks. 
2. If all dictionaries created by the tasks are stored in the same dropbox folder then a program based upon the file names can sort the files into lists that pertain to a particular data frame to be populated. 
3. For each file within the lists just described a data frame could be created along the lines of the template frame
4. All of those data frames would be concatenated together
5. This data frame would then be concatenated with the master data frame / each update would be separately saved for concatenation at a later date. 

###Store Observations
CCC: Will observations be stored in a SQL database?
RC: At this time I think I SQL is surplus to requirements. Perhaps if when the project moves beyond pilot this could be considered. As I have no experience with SQL I feel that it might be an additional learning curve I have to scale when there might be more important ones close at hand...

###Backup Obesrvations
CCC: Timestamped versions of the Observation database will be copied to Dropbox
RC: Are you thinking to maintain one master database, or a separate databases for each update? Given what you said about data loss, I am assuming the latter. Is that right? 

###Report on Observations
CCC: Who needs to see Observation reports and in what format?
RC: Me. I would need an indication of what tasks were succesfully completed on which days, and obviously I would have access to the dropbox to view the master data files.

RC: One general comment is that as there is only one person pulling the strings on this project (me) it might not be so essential that this back-end workflow is integrated into the application itself. Additionally as Pythonista does not support pandas, I suspect that I will have to create routines that run outside of the pythonista framework in order to work with this data. 
