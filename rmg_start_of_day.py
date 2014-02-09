# RMG_set_machine_counts.py

import bottle, console, json, pprint, sys, thread, threading, time, webbrowser

#Thanks for this. I have some comments:
# 1. Since I am new to a lot of this material it would be really useful for me if you could include brief docstrings
# or comments, just so that I can follow along.

# 2. I do not think all 'teams' should be on the same form. I do not want to compel the user to necessarily do all 
# of them at the same time. Additionally, the sections may be very far away from each other. Lastly, I feel that
# doing it team by team will allow for a nicer layout, and prevent larger scale data loss which may be useful for the
# end user. 

#3. I see how managing the URL by using globals works, but is this the only option? 

# 4. I prefer to have the user state if the machine is manned or unmanned. I feel that leaving blank to indicate
# unmanned is too passive and could lead to error.

# 5. How can I now check that all machines have been filled in to satisfaction? I need to return messages to the user.
# ideally the relevant table cell would be highlighted red. Would this use a PUT method?

# 6. See the .tpl file I created that i believe helps to achieve a good layout. It accepts the rmg_machine_operators
# dict and an indication of what team is being followed at that moment. This could be determined by the console 
# commands. 

# As a general question how do you return incorrect data to the user without them having to rerun the program? I am
# having difficulty figuring this out. 

machine_operators_file_name = 'rmg_machine_operators.json'

done = False

RMG_machine_operators = None

def short_key(in_long_key):  # returns KT for input knitting_treatment
    the_key = in_long_key.upper().split('_')  # KNITTING, TREATMENT
    return the_key[0][0] + the_key[1][0]      # KT, KS, KD, LT, LS, LD
    
def get_worker_entry_dict(source_dict = RMG_machine_operators):
    html_table_fmt     = '''
<table border="1">
    <tr>{}
    </tr>
</table>'''
    html_table_row_fmt = '''
        <td>{}{}</td>
        <td><input type="text" name="{}{}" value="{}"></td>'''
    dest_dict = {}  # empty dict
    # <input type="number" name="knitting_treatment">
    for i, key in enumerate(source_dict):
        print(key)
        group_key = short_key(key)  # convert knitting_treatment --> KT
        table_rows = [html_table_row_fmt.format(group_key, i+1, group_key, i, x)
                        for i, x in enumerate(source_dict[key])]
        dest_dict[key] = html_table_fmt.format(''.join(table_rows))
        print(dest_dict[key])
    return dest_dict

@bottle.get('/start_of_day')
def get_start_of_day():
    return '''
<div style="text-align:center;">
    <h1>Ready Made Garments:  Start of Day</h1>
    <h3>Please enter the operator in next to each machine below and then tap the "Submit" button.</h3>
    <h4>Leave the field blank for any machines which are not manned.<h4>
</div>
<p>
<form action="/start_of_day" method="post">
    Knitting Treatment Group:      <br>{knitting_treatment}<br>
    Knitting Same Floor Group:     <br>{knitting_same_floor}<br>
    Knitting Different Floor Group:<br>{knitting_different}
    <p>
    Linking Treatment Group:       <br>{linking_treatment}<br>
    Linking Same Floor Group:      <br>{linking_same_floor}<br>
    Linking Different Floor Group: <br>{linking_different}
    <p>
    <div style="text-align:center;">
        <input value="Submit" type="submit" />
    </div>
</form>'''.format(**get_worker_entry_dict(RMG_machine_operators))

@bottle.post('/start_of_day')
def post_start_of_day():
    check_results(bottle.request.forms)

@bottle.get('/start_of_day/success')
def get_start_of_day_success():
    return '''
<div style="text-align:center;">
    <h1>Ready Made Garments:  Start of Day</h1>
    <p>
    <h1>Tap the "Done" button to finish...</h1>
</div>'''

def flatten_dict(in_long_keys, in_dect):
    out_dect = {}  # empty dict
    for long_key in in_long_keys:
        the_list = []  # empty list
        group_key = short_key(long_key)
        for i in xrange(99):
            the_key = group_key + str(i)
            if the_key in in_dect:
                the_list.append(in_dect[the_key].strip())
            else:
                break
        out_dect[long_key] = the_list
    return out_dect

def check_results(in_dict):
    global done, valid_input
    out_dict = flatten_dict(RMG_machine_operators.keys(), in_dict)
    with open(machine_operators_file_name, 'w') as out_file:
        json.dump(out_dict, out_file)
    done = True

def web_client(in_url = 'http://localhost:8080/start_of_day'):
    webbrowser.open(in_url)
    while not done:
        time.sleep(1)
    webbrowser.open(in_url + '/success', stop_when_done=True)
    time.sleep(1)

def load_machine_operators(in_file_name = machine_operators_file_name):
    global RMG_machine_operators
    try:
        with open(in_file_name) as in_file:
            RMG_machine_operators = json.load(in_file)
    except IOError:
        RMG_machine_operators = None
    return RMG_machine_operators

def main(argv):
    if not load_machine_operators(machine_operators_file_name):
        return 'File not found: ' + machine_operators_file_name
    threading.Thread(None, web_client).start()
    bottle.run(quiet=True)  # run a web server until interrupted
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
