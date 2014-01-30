# Work In Progress (WIP) Task

### Background and Purpose
Outside of this application the research team responsible for this pilot project will be collecting production data relating to the teams (both in knitting and linking sections) that are being observed. This production data will be used to measure efficiency of the factory teams over time. However, this data is lacking in a very important way, and this drives the need for this task. The issue is that workers may 'hand in' up to 48 pieces at a time in multiples of 12. The receipt of these bundles of 12 is recorded in the production data. However, as 12/24/36/48 pieces can take some days to complete recording the number of pieces as work in progress (meaning not yet handed in) is critical to understanding how productive a worker is on a day to day basis. 

### Measuring WIP

#### Knitting Section <br />
In a sense wip in the knitting section should be measured in increments of 0.25 for the knitting section. This is because a sweater is comprised of four panels (front, back, sleeve1, sleeve2). Each of these four panels is knitted by a single operator. 

One confounding factor is that the machines are set up such that the operators can knit one full bundle of a particular panel (e.g. back) before they then re-calibrate the machine to being the next panel (e.g. sleeve1). There is some difference in the amount of time, effort and operations that go into producing each different panel. 

Given the above, it seems clear that conceptualising wip in units of 0.25 is an error. This is because if an operator has knitted four sleeves then he has not in any sense knitted one 'piece'. 

This indicates that the wip should be measured in terms of completed panels. i.e. the (whole) number of completed back panels, the (whole) number of completed front panels etc.

One final consideration is that the four panels constitute the 'body' of the sweater. However, there is a final component that is created in the knitting section: the collar. 

The collar is different from the body [we assume because the machine requires a totally different sort of calibration], and as such there will be operators that only knit collars. That is at any point in time some operators will be working on body (four panels) and some will be working on collars. It is not the case therefore that some operators are designated as collar knitters. 

All of this indicates that wip should be measured in whole integer units, and in the case of those operators working on body pieces a count of the different panels should be undertaken to get the best possible measure of wip.

For the sake of clarity note that WIP is the number of pieces completed but not handed in.

**Caveat** At present it is not clear if there is any physical difference between sleeve1 and sleeve2. If there is then the wip for each will be separately recorded (sleeve1, sleeve2), if not then the wip be simply recorded for sleeve. At present it is assumed there is a physical difference. 

#### Linking Section <br />
Similarly the linking section wip could be measured in increments of 0.25. The linking operators have to complete four major processes in that they have to link together five parts (the four body panels with the collar). Thinking in terms of increments of 0.25 pieces is less problematic for this section, and should therefore be preserved. 

###Data Structure
The above leads to the conclusion that there are three potential data structures that will capture differenced within and between sections. The are as follows:

+ Knitting Body
+ Knitting Collar
+ Linking

However, for the sake of ease the knitting sections wip data structure should be singular, but the structure should be flexible enough to be able to cope with workers that are working on body or collars. 

Rather than conceptualising the unit of observation as an individual, the unit of observation will be a machine within then team (as these are fixed - see Readme.md). The mc_status of teahc machine ('Manned' or 'Unmanned') will be determined during the id_dict routine, and the data that this routine generates will be shared with all tasks including the wip task. One necessary extension of this will a sub-routine that allows the user to make changes to the id_dict data if when undertaking the wip task the information collected during the id_dict routine is not longer accurate e.g. if a machine in unmanned in the morning, but manned in the afternoon (due to operator tardiness).

* Knitting team wip data structure:

		Knitting_WIP_dict = { 'DateTime' : '01/14/2014 14:36',
							  'KN1'      : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'component'  : 'body'
											 'back' 	  : 12,
											 'front'	  : 12,
											 'sleeve1'	  : 12,
											 'sleeve2'	  : 8,
											 'collar'	  : 'null' }
								   
							  'KN2'	     : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'component'  : 'collar',
											 'back' 	  : 'null',
											 'front'	  : 'null',
											 'sleeve1'	  : 'null',
											 'sleeve2'	  : 'null',
											 'collar'	  : 32 	   }
								   								   
							  'KN3'	     : { 'mc_status'  : 'Unmanned',
											 'worker_id'  : 'null',
											 'Style'      : 'null',
											 'component'  : 'null',
											 'back' 	  : 'null',
											 'front'	  : 'null',
											 'sleeve1'	  : 'null',
											 'sleeve2'	  : 'null',
											 'collar'	  : 'null' } }

**NB** The mc_status variable will be determined by the worker_id routine that should also be completed by the user. For more information about this routine see the 'Other Functionality' section in Readme.md

* Linking team wip data structure: 

		Linking_WIP_dict =  { 'DateTime' : '01/14/2014 14:36',
							  'LI1'      : { 'mc_status'  : 'Manned',
											 'worker_id'  : 'foo',
											 'Style'      : 'bar',
											 'wip'	      : 4.25 }

							  'LI2'      : { 'mc_status'  : 'Unmanned',
											 'worker_id'  : 'null',
											 'Style'      : 'null',
											 'wip'	      : 'null'}

Initially it was thought by RC that one master dictionary would be created which would be iteratively added to once each wip task was completed. This is not a healthy plan as it could lead to big problems of data loss. On the suggestion of CCC this will be reduced, although not all the way to one file per observation, but one file per completed task. Therefore each time the task is completed for all members of the team being observed a json file will be saved to dropbox  that contains the data for the enitre section of machines under observation. 
											 
											 
											 