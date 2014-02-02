# rmg_start_of_day.py

import bottle, console, json, sys, thread, threading, time, webbrowser

machine_operators_file_name = 'RMG_machine_operators.json'

done = valid_input = False

RMG_machine_operators = None

def get_worker_entry_dict(source_dict = RMG_machine_operators):
    html_table_fmt     = '''
<table border="1">
    <tr>{}    </tr>
</table>'''
    html_table_row_fmt = '''
        <td>{}{}</td>
        <td><input type="text" name="{}{}" value="{}"></td>
'''
    dest_dict = {}  # empty dict
    # <input type="number" name="knitting_treatment">
    for i, key in enumerate(source_dict):
        group_key = key.upper().split('_')             # KNITTING, TREATMENT
        group_key = group_key[0][0] + group_key[1][0]  # KT, KS, KD, LT, LS, LD
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
    count_dict = { 'tab' : '&nbsp;' * 30 }
    for key in RMG_machine_operators:
        count_dict[key] = len(RMG_machine_operators[key])
    return '''
<div style="text-align:center;">
    <h1>Ready Made Garments:  Tap the "Done" button to finish...</h1>
</div>
<p>
<h3>{tab}Knitting Treatment Group has {knitting_treatment} machines.</h3>
<h3>{tab}Knitting Same Floor Group has {knitting_same_floor} machines.</h3>
<h3>{tab}Knitting Different Floor Group has {knitting_different} machines.</h3>
<p>
<h3>{tab}Linking Treatment Group has {linking_treatment} machines.</h3>
<h3>{tab}Linking Same Floor Group has {linking_same_floor} machines.</h3>
<h3>{tab}Linking Different Floor Group has {linking_different} machines.</h3>
'''.format(**count_dict)

@bottle.get('/start_of_day/failure')
def get_start_of_day_failure():
    return '''
<div style="text-align:center;">
    <h1>Ready Made Garments:  Tap the "Done" button to finish...</h1>
    <p>
    <h1>All 6 values must be integers.  Please rerun.</h1>
</div>'''

def check_results(in_dict):
    global done, valid_input
    for the_key in in_dict:
        try:
            the_value = int(in_dict[the_key])
        except ValueError:
            print('All 6 values must be integers.  Please rerun.')
            done = True
            return  # web_client()  # check_results(in_dict)
        valid_input = True
        RMG_machine_operators[the_key] = tuple([None for i in xrange(the_value)])
    print(RMG_machine_operators)
    with open('RMG_machine_operators.json', 'w') as out_file:
        json.dump(RMG_machine_operators, out_file)
    done = True

def web_client(in_url = 'http://localhost:8080/start_of_day'):
    webbrowser.open(in_url)
    while not done:
        time.sleep(1)
    the_url = in_url + ('/success' if valid_input else '/failure')
    print(the_url)
    webbrowser.open(the_url, stop_when_done=True)
    time.sleep(1)
    ##console.hud_alert('Please tap "Done" in the upper right...')
    #thread.interrupt_main()

def load_machine_operators():
    global RMG_machine_operators
    try:
        with open(machine_operators_file_name) as in_file:
            RMG_machine_operators = json.load(in_file)
    except KeyboardInterrupt:
        RMG_machine_operators = None
    return RMG_machine_operators

def main(argv):
    if not load_machine_operators():
        return
    threading.Thread(None, web_client).start()
    bottle.run()  # quiet=True)  # run a web server until interrupted
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
