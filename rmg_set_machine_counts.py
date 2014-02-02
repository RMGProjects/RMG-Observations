# RMG_set_machine_counts.py

import bottle, console, json, sys, thread, threading, time, webbrowser

done = valid_input = False

RMG_machine_operators = { 'knitting_treatment'  : [],
                          'knitting_same_floor' : [],
                          'knitting_different'  : [],
                          'linking_treatment'   : [],
                          'linking_same_floor'  : [],
                          'linking_different'   : [] }

@bottle.get('/machine_counts')
def get_machine_counts():
    return '''
<div style="text-align:center;">
    <h1>Ready Made Garments:  Set Machine Counts</h1>
    <h3>Please enter six integer values below and then tap the "Submit" button.</h3>
</div>
<p>
<form action="/machine_counts" method="post">
    Knitting Treatment Group has <input type="number" name="knitting_treatment"> machines.<br>
    Knitting Same Floor Group has <input type="number" name="knitting_same_floor"> machines.<br>
    Knitting Different Floor Group has <input type="number" name="knitting_different"> machines.
    <p>
    Linking Treatment Group has <input type="number" name="linking_treatment"> machines.<br>
    Linking Same Floor Group has <input type="number" name="linking_same_floor"> machines.<br>
    Linking Different Floor Group has <input type="number" name="linking_different"> machines.
    <p>
    <input value="Submit" type="submit" />
</form>'''

@bottle.post('/machine_counts')
def post_machine_counts():
    check_results(bottle.request.forms)

@bottle.get('/machine_counts/success')
def get_machine_counts_success():
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

@bottle.get('/machine_counts/failure')
def get_machine_counts_failure():
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

def web_client(in_url = 'http://localhost:8080/machine_counts'):
    webbrowser.open(in_url)
    while not done:
        time.sleep(1)
    webbrowser.open(in_url + ('/success' if valid_input else '/failure'))
    time.sleep(1)
    #console.hud_alert('Please tap "Done" in the upper right...')
    thread.interrupt_main()
        
def main(argv):
    threading.Thread(None, web_client).start()  # start a web browser
    try:
        bottle.run(quiet=True)  # run a web server until interrupted
    except KeyboardInterrupt:   # browser thread will trigger this interrupt
        pass
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
