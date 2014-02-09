<div style="text-align:center;">
    <h1>Ready Made Garments:  Collection IDs of Machine Operators</h1>
	<h2>Team : {{team.split('_')[0].capitalize() + ' ' + team.split('_')[1].capitalize()}}</h2>
    <h3>For each machine please state if the machine is 'Manned' or 'Unmanned'</h3>
    <h3>If the machine is manned also enter the ID number of the operator (as per the operator's identification card)'<h4>
</div>


<p>
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
	<input type="radio" id = "radio{{str(id_counter)}}" name="mc_status{{str(id_counter)}}" value="unmanned" onclick = "
	if (this.checked) {
		document.getElementById('ID{{str(id_counter)}}').style.visibility = 'hidden';
		document.getElementById('TEXT{{str(id_counter)}}').style.visibility = 'hidden';}
	return true;">Unmanned<br>
		
	<input type="radio" id = "radio{{str(id_counter)}}" name="mc_status{{str(id_counter)}}" value="manned" onclick = "
	if (this.checked) {
		document.getElementById('ID{{str(id_counter)}}').style.visibility = 'visible';
		document.getElementById('TEXT{{str(id_counter)}}').style.visibility = 'visible';} 
	return true;">Manned<br>
	
	<html: 'Operator Id' id = 'TEXT{{str(id_counter)}}'>Operator ID<INPUT TYPE="TEXT" NAME="in_id{{str(id_counter)}}" SIZE="20" id = 'ID{{str(id_counter)}}'>
	</td>
	%id_counter+=1
%end
</tr>
</table>
</form>

<button onclick = "validateForm()">Validate Data</button> : Always validate the data until there are no more errors before submitting
<p> <br> </p>
<p id="error_message"><br></p>

<script>
function validateForm(){
	var x="";
	for (var i=1; i<=parseInt({{no_machines}}); i++) {
		var in_id=document.forms["simple_form"]["ID" + i].value;
		var in_choice = getCheckedRadio(i);

		if (in_choice == undefined){
			x = x + "Please select a machine status for KN" + i + "<br>";
			document.getElementById("error_message").innerHTML=x;}

		if (in_choice == 'unmanned'){
			document.getElementById('ID' + i).value = null;}

		if (in_choice == 'manned' && (in_id =="" || in_id==null)){
			x = x + "Machine KN" + i + " is manned, either enter an operator ID or change machine status" + "<br>";
			document.getElementById("error_message").innerHTML=x;}

		if (in_choice == 'unmanned' && (in_id !="" || in_id!=null)){
			x = x + "Machine KN" + i + " is manned, either enter an operator dfsfsdfID or change machine status" + "<br>";
			document.getElementById("error_message").innerHTML=x;}

		if (in_id==null || in_id==""){
			x = x + "Do not leave person KN" + i + " empty" + "<br>";
			document.getElementById("error_message").innerHTML=x;}

	}
}
</script>

<script>
function getCheckedRadio(i) {
     var radioButtons = document.getElementsByName("mc_status" + i);
     for (var z = 0; z < radioButtons.length; z ++) {
     if (radioButtons[z].checked) {
       
       choice = radioButtons[z].value;
       return choice;
     }
     }
  }
</script>