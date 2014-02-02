# -*- coding: utf-8 -*-

'''
<<<<<<< HEAD
RMG_utils.py -- these utility functions are used by the Ready–Made Garments (RMG) Observation script(s).
=======
RMG_utils.py -- these utility functions are used by the Readyâ€“Made Garments (RMG) Observation script(s).
>>>>>>> 9ece0a901d77f7495c52eb2a02165a042bcab486
    These functions are not specific to RMG use cases but instead are general enough to be useful in
    other contexts.   We have therefore placed them in this separate file to increase the likelihood of
    reuse.  This approach should reduce both the size and the complexity of RMG_specific scripts.
'''

import console, datetime, json, pprint, sys, time, Image, photos

def get_timestamp(in_datetime = None):
    ''' Returns formatted date string
            If the caller provides a datetime then it will be used.
            If the caller provides None the current time will be used. '''
    in_datetime = in_datetime or datetime.datetime.now()
    return in_datetime.strftime('%Y_%m_%d_%H_%M')

def get_user_choice(in_title, in_prompt, in_choices, in_allow_cancel = True):
    ''' Returns the text of user's choice from multiple choices '''
    try:
        return in_choices[console.alert(in_title, in_prompt, *in_choices) - 1]
    except KeyboardInterrupt:
        if in_allow_cancel:
            raise  # let someone higher up deal with the exception (or not)
        else:
            pass   # prevent the user from cancelling the script
    console.hud_alert('You are not allowed to cancel this operation.', 'error')
    return get_user_choice(in_title, in_prompt, in_choices, in_allow_cancel)

def get_user_input(in_prompt, in_allow_cancel = True):
    ''' Returns a text string entered by the user '''
    try:
        return console.input_alert(in_prompt)
    except KeyboardInterrupt:
        if in_allow_cancel:
            raise  # let someone higher up deal with the exception (or not)
        else:
            pass   # prevent the user from cancelling the script
    console.hud_alert('You are not allowed to cancel this operation.', 'error')
    return get_user_input(in_prompt)

def get_user_integer(in_prompt, in_min = 0, in_max = 100000, in_allow_cancel = True):
    ''' Returns an integer entered by the user '''
    (in_min, in_max) = (int(min(in_min, in_max)),  # verify that in_min and in_max are both
                        int(max(in_min, in_max)))  #  integers and than in_min is <= in_max
    try:
        user_int = int(get_user_input(in_prompt, in_allow_cancel))
        if in_min <= user_int <= in_max:
            return user_int
    except ValueError:
        pass
    fmt = 'Error: Please enter a whole number between {} and {}'
    console.hud_alert(fmt.format(in_min, in_max), 'error')
    return get_user_integer(in_prompt, in_min, in_max, in_allow_cancel)

def get_user_float(in_prompt, in_min = 0.0, in_max = 100000.0, in_allow_cancel = True):
    ''' Returns an float entered by the user '''
    (in_min, in_max) = (float(min(in_min, in_max)),  # verify that in_min and in_max are both
                        float(max(in_min, in_max)))  #  floats and than in_min is <= in_max
    try:
        user_float = float(get_user_input(in_prompt, in_allow_cancel))
        if in_min <= user_float <= in_max:
            return user_float
    except ValueError:
        pass
    fmt = 'Error: Please enter a floating point number between {} and {}'
    console.hud_alert(fmt.format(in_min, in_max), 'error')
    return get_user_float(in_prompt, in_min, in_max, in_allow_cancel)

def get_user_special_float(in_prompt, in_min = 0.25, in_max = 48.0, in_allow_cancel = True):
    ''' Returns an float entered by the user only if it is a multiple of 0.25 '''
    user_float = get_user_float(in_prompt, in_min, in_max, in_allow_cancel)
    if not (user_float % 0.25):  # user_float is an even multiple of 0.25
        return user_float
    fmt = 'Error: Please enter a number between {} and {} that is a multiple of 0.25'
    console.hud_alert(fmt.format(in_min, in_max), 'error')
    return get_user_special_float(in_prompt, in_min, in_max, in_allow_cancel)

def get_user_photo(in_allow_none = True):
    ''' Prompts the user to take a photo and returns the image '''
    user_photo = photos.capture_image()
    if user_photo or in_allow_none:
        return user_photo
    Error = 'You are not allowed to cancel taking the photograph at this time.'
    console.hud_alert(Error, 'error')
    return get_user_photo(in_allow_none)

def save_user_photo(photo, task_name):
    ''' Saves a user photo with the name of the related task and a timestamp
            This can be used as proof that a particular iOS device
            was at a particular location at a particular time.
            GPS Location was not used because of intermittent Internet access. '''
    if photo:
        task_name = task_name.replace(' ', '_') if task_name else 'photo'
        photo.save('{}_{}.jpg'.format(task_name.replace(' ', '_'), get_timestamp()))

def main(argv):
    console.clear()
    print('Testing utility functions')
    # get_timestamp(in_datetime = None)
    print(get_timestamp())
    print(get_timestamp(datetime.datetime.strptime('02/13/1970', '%m/%d/%Y')))
    # get_user_choice(in_title, in_prompt, in_choices, in_allow_cancel = True)
    print(get_user_choice('get_user_choice()', 'prompt -- can cancel', ('1', '2', '3')))
    print(get_user_choice('get_user_choice()', 'prompt -- can not cancel', ('1', '2', '3'), False))
    # get_user_input(in_prompt, in_allow_cancel = True)
    print(get_user_input('get_user_input() -- can cancel'))
    print(get_user_input('get_user_input() -- can not cancel', False))
    # get_user_integer(in_prompt, in_min = 0, in_max = 100000, in_allow_cancel = True)
    print(get_user_integer('get_user_integer() -- can cancel', 1, 10))
    print(get_user_integer('get_user_integer() -- can not cancel', 1, 10, False))
    # get_user_float(in_prompt, in_min = 0.0, in_max = 100000.0, in_allow_cancel = True)
    print(get_user_float('get_user_float() -- can cancel', 1.0, 10.0))
    print(get_user_float('get_user_float() -- can not cancel', 1.0, 10.0, False))
    # get_user_special_float(in_prompt, in_min = 0.25, in_max = 48.0, in_allow_cancel = True)
    print(get_user_special_float('get_user_special_float() -- can cancel', 1.0, 10.0))
    print(get_user_special_float('get_user_special_float() -- can not cancel', 1.0, 10.0, False))
    # get_user_photo(in_allow_none = True) and save_user_photo(photo, task_name)
    print('get_user_photo() -- allow None')
    save_user_photo(get_user_photo(), 'My task name')
    print('get_user_photo() -- do not allow None')
    save_user_photo(get_user_photo(False), None)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
