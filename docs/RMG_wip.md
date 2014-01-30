# Work In Progress (WIP) Task

### Background and Purpose
Outside of this application the research team responsible for this pilot project will be collecting production data relating to the teams (both in knitting and linking sections) that are being observed. This production data will be used to measure efficiency of the factory teams over time. However, this data is lacking in a very important way, and this drives the need for this task. The issue is that workers may 'hand in' up to 48 pieces at a time in multiples of 12. The receipt of these bundles of 12 is recorded in the production data. However, as 12/24/36/48 pieces can take some days to complete recording the number of pieces as work in progress (meaning not yet handed in) is critical to understanding how productive a worker is on a day to day basis. 

<br />
### Measuring WIP

#### Knitting Section
In a sense wip in the knitting section should be measured in increments of 0.25. This is because a sweater is comprised of four panels (front, back, sleeve1, sleeve2). Each of these four panels is knitted by a single operator. 

One confounding factor is that the machines are set up such that the operators can knit one full bundle of a particular panel (e.g. back) before they then re-calibrate the machine to begin the next panel (e.g. sleeve1). There is some difference in the amount of time, effort and operations that go into producing each different panel. 

Given the above, it seems clear that conceptualising wip in units of 0.25 is an error. This is because if an operator has knitted four sleeves then he has not in any sense knitted one 'piece'. 

This indicates that the wip should be measured in terms of completed panels. i.e. the (whole) number of completed back panels, the (whole) number of completed front panels etc.

An additional consideration is that the four panels constitute the 'body' of the sweater. However, there is a final component that is created in the knitting section: the collar. 

The collar is different from the body [we assume because the machine requires a totally different sort of calibration], and as such there will be operators that only knit collars. That is at any point in time some operators will be working on body (four panels) and some will be working on collars. It is not the case therefore that some operators are designated as collar knitters for all time. 

All of this indicates that wip should be measured in whole integer units, and in the case of those operators working on body pieces a count of the different panels should be undertaken to get the best possible measure of wip.

There are two final things to consider. Firstly in the majority of cases sleeve1 and sleeve2 are identical in terms of the processes and machine configuration. However in some cases they will be different if they have different designs. However, this distinction is not one that I am willing to make during the recording process as it is too nuanced. This will introduce some error into the data, but a level of error I am happy to deal with. Therefore the data collected will simply be for number of sleeves. 

Secondly, and more perniciously there are certain complex styles where a certain panel may be knitted not by the knitting operators but an automatic machine. This will be the case if the front panel (e.g.) is extremely complex and beyond manual knitting. This means that for some styles there will be panels that are knitted elsewhere, and therefore for these sections a None option should be available for each different panel. 

For the sake of clarity note that WIP is the number of pieces completed but not handed in.

<br />
#### Linking Section
Similarly the linking section wip could be measured in increments of 0.25. The linking operators have to complete four major processes in that they have to link together five parts (the four body panels with the collar). Thinking in terms of increments of 0.25 pieces is less problematic for this section, and should therefore be preserved. 

<br />
###Data Structure
The above leads to the conclusion that there are three potential data structures that will capture differences within and between sections. The are as follows:

+ Knitting Body
+ Knitting Collar
+ Linking

However, for the sake of ease the knitting sections wip data structure should be singular, but the structure should be flexible enough to be able to cope with workers that are working on body or collars. 

Rather than conceptualising the unit of observation as an individual, the unit of observation will be a machine within then team (as these are fixed - see Readme.md). The mc_status of each machine ('Manned' or 'Unmanned') and the 'worker_id' will be determined during the id_dict routine, and the data that this routine generates will be shared with all tasks including the wip task. One necessary extension of this will be a sub-routine that allows the user to make changes to the id_dict data when undertaking the wip task if the information collected during the id_dict routine is no longer accurate e.g. if a machine in unmanned in the morning, but manned in the afternoon (due to operator tardiness).

* Knitting team wip data structure:

		Knitting_WIP_dict = { 'DateTime' : '01/14/2014 14:36',
							  'KN1'      : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'component'  : 'body'
											 'back' 	  : 12,
											 'front'	  : 12,
											 'sleeve'	  : 7,
											 'collar'	  : None }
											 
							  'KN2'      : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'component'  : 'body'
											 'back' 	  : 24,
											 'front'	  : None
											 'sleeve'	  : 6,
											 'collar'	  : None }
								   
							  'KN3'	     : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'component'  : 'collar',
											 'back' 	  : None,
											 'front'	  : None,
											 'sleeve'	  : None,
											 'collar'	  : 32 	   }
								   								   
							  'KN4'	     : { 'mc_status'  : 'Unmanned',
											 'worker_id'  : None,
											 'Style'      : None,
											 'component'  : None,
											 'back' 	  : None,
											 'front'	  : None,
											 'sleeve'	  : None,
											 'collar'	  : None } }

Regarding the above examples machine KN1 is manned and producing body (all panels); KN2 is manned and producing all panels except 'front' (which is presumably produced upstairs - see above); KN3 is manned and producing collar; KN4 is unmanned. 

											 
* Linking team wip data structure: 

		Linking_WIP_dict =  { 'DateTime' : '01/14/2014 14:36',
							  'LI1'      : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'wip'	      : 4.25 }

							  'LI2'      : { 'mc_status'  : 'Unmanned',
											 'worker_id'  : None,
											 'Style'      : None,
											 'wip'	      : None}

Initially it was thought by RC that one master file would be created which would be iteratively added to once each wip task was completed. This is not a healthy plan as it could lead to big problems of data loss. On the suggestion of CCC this will be reduced, although not all the way to one file per observation, but one file per completed task. Therefore each time the task is completed for all members of the team being observed a json file will be saved to dropbox  that contains the data for the enitre section of machines under observation. 
											 
											 
											 