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
        

In the factories under observation, the observer (i.e. the user of this application) will be present daily, and they will follow a strict diary of the tasks that need to be completed. The tasks will always relate to the same group of knitting/linking operators throughout the duration of the project. Therefore, upon first opening the application, the numbers to be followed, and their ID codes etc need to be determined/input

The observations are strictly controlled i.e. should not provide felxibility to the user as to what data are entered once a task is begun. If a task is begun then it must be completed for every operator for which there is an id code. If a data point is not reuqired for an opeartor under observation, then a null value should be entered and it should be clear from the data structure as to why that data point was not required.


**Tasks:** Currently two tasks are contemplated although the application has a lot of potential to be expanded. at present the application should be written such that future tasks can be added:

1. **Measuring WIP** - at two points during the day, the user must record the amount of work in progress. Workers may 'hand in' up to 36 pieces at a time in multiples of 12. The receipt of these bundles of 12 is recorded elsewhere. However, as 12/24/36 pieces can take some days to complete recording the number of pieces as work in progress (meaning not yet handed in) is critical to understanding how productive a worker is on a day to day basis.

    For the sake of clarity note that WIP is the number of pieces completed but not handed in.

2. **Recording Interactions** - the scope of this task is not yet fully defined. The basic idea is that for a fixed amount of time the observer will follow a supervisor and record the interaction that he has with the knitting operators.

**Output:** There are two levels of output currently envisaged: Top Level Ouput and Task Level Output.

The Top Level Output is a dictionary saved as a .json of the following format:

    TopLevelDict = { 'Knitters' : [],
                     'Linkers'  : [] }

This output will be created upon first opening (user configuring) the application.

The Task Level Output will vary by task, although data will be stored in dictionaries and saved a .json files:

* Measuring WIP (example given in the knitting section with id code KN1, KN2 etc.:

    WIPDict = { 'DateTime' : '01/14/2014 14:36',
                'KN1'      : { 'Attendance' : 'Present',
                               'Style'      : 7,
                               'WIP'        : 4.25 },
                'KN2       : { 'Attendance' : 'Present',
                               'Style'      : 'Grunge',
                               'WIP'        : 0.75 }
              }

Similar output should be generated for all tasks implemented in this application.
