1. Remove the attendance component of the WIP task as this will be determined by the id_dict routine

2. Add a component to the WIP that allows the id_dict to be modified if a change in the mc_status has occurred since undertaking the id_dict routine (see RMG_wip.md for details)

3. Add a level of detail to the WIP dict that asks the user to enter state whether the operator is working on the body or the collar, and if body then to input wip for each panel (see RMG_wip.md for details)

4. A) Rework the start_of_day program to implement the id_template - I feel that this layout will be more readable and user friendly.
   B) Rework the program so that the user has to choose which team to enter data for. I do not want them all presented as the same time as the units may be physically distant, and the more data there is to enter at one time the greater the risk that some of it will get lost. 