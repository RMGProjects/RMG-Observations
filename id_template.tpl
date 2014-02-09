<div style="text-align:center;">
    <h1>Ready Made Garments:  Collection IDs of Machine Operators</h1>
	<h2>Team : {{team.split('_')[0].capitalize() + ' ' + team.split('_')[1].capitalize()}}</h2>
    <h3>For each machine please state if the machine is 'Manned' or 'Unmanned'</h3>
    <h3>If the machine is manned also enter the ID number of the operator (as per the operator's identification card)	'<h4>
</div>
<p>
<br/>
<form action="/start_of_day" method="post">
<TABLE BORDER="3">
% no_machines = len(RMG_machine_operators[team])
% id_counter = 1
% team_code = (team.split('_')[0][0] + team.split('_')[1][0]).upper()
<tr>
%for machine in xrange(no_machines):
	%if (id_counter - 1)%8.0 == 0:
		</tr>
		<tr>
	%end
	
	<td>{{team_code + str(id_counter)}}</td>
	<td>   
	<input type="radio" id = "radio{{str(id_counter)}}" name="mc_status" value="unmanned" onclick = "
	if (this.checked) {
		document.getElementById('ID{{str(id_counter)}}').style.visibility = 'hidden';
		document.getElementById('TEXT{{str(id_counter)}}').style.visibility = 'hidden';}
	return true;">Unmanned<br>
		
	<input type="radio" id = "radio{{str(id_counter)}}" name="mc_status" value="manned" onclick = "
	if (this.checked) {
		document.getElementById('ID{{str(id_counter)}}').style.visibility = 'visible';
		document.getElementById('TEXT{{str(id_counter)}}').style.visibility = 'visible';} 
	return true;">Manned<br>
	
	<html: 'Operator Id' id = 'TEXT{{str(id_counter)}}'>Operator ID<INPUT TYPE="TEXT" NAME="name" SIZE="20" id = 'ID{{str(id_counter)}}'>
	</td>
	%id_counter+=1
%end
</tr>
