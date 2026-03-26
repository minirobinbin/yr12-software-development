"""This script launches a GUI application that displays records of rangers."""

import FreeSimpleGUI as sg

def create_gui() -> sg.Window:
    """
    Constructs the layouts and window for the GUI.
    :return: the window for the GUI   
    """
    # Create the GUI.
    record_layout = [[sg.Text('First name:'),
                      sg.Text('xx', key='-FIRST_NAME_LABEL-', font='default 10 bold')],
                     [sg.Text('Last name:'),
                      sg.Text('xx', key='-LAST_NAME_LABEL-', font='default 10 bold')],
                     [sg.Text('Date of birth:'),
                      sg.Text('xx', key='-DOB_LABEL-', font='default 10 bold')],
                     [sg.Text('Area of expertise:'),
                      sg.Text('xx', key='-EXPERTISE_LABEL-', font='default 10 bold')],
                     [sg.Text('Current employee:'),
                      sg.Text('xx', key='-EMPLOYED_LABEL-', font='default 10 bold')]]
    navigate_layout = [[sg.Frame('Ranger', record_layout, expand_x=True, size=(250,200), )],
                       [sg.Button('Previous', key='-PREVIOUS_BUTTON-', size=8, disabled=True),
                        sg.Text('000', key='-INDEX_LABEL-', auto_size_text=False, size=3,
                            justification='center', font='default 10 bold'),
                        sg.Button('Next', key='-NEXT_BUTTON-', size=8, disabled=True)]]
    search_layout = [[sg.Input('', key='-SEARCH_TEXTBOX-')],
                     [sg.Button('Search')]]
    sort_layout = [[sg.Button('Sort by last name', size=20)],
                   [sg.Button('Sort by expertise', size=20)]]
    sort_and_search_layout = [[sg.Frame('Search', search_layout, pad=((7, 7), (5, 10)))],
                              [sg.Frame('Sort', sort_layout)]]
    layout = [[sg.Frame('', navigate_layout, border_width=0),
               sg.Frame('', sort_and_search_layout, border_width=0, vertical_alignment='top')]]
    return sg.Window('Ranger Viewer', layout, element_padding=((7, 7), (5, 5)))


def perform_search(records: list, text: str) -> int:
    """
    Performs a search for text in the first names and last names of the ranger records.
    :param records: the list of dictionaries to search
    :param text: the text to search for
    :return: the index of the first record containing the text, or -1 if not found
    """
    for record in records:
        if text.lower() in record['first name'].lower() or text in record['last name'].lower():
            return records.index(record)
    return -1


def sort_by_last_name(records: list) -> list:
    """
    Performs a simple selection sort of the list of ranger records by last name.
    :param records: the list of dictionaries to sort
    :return: a new sorted list
    """
    sorted_records = []
    full_length = len(records)
    while len(sorted_records) < full_length:
        lowest = records[0]
        for record in records:
            if record['last name'] < lowest['last name']:
                lowest = record
        sorted_records.append(lowest)
        records.remove(lowest)
    return sorted_records


def sort_by_expertise(records: list) -> list:
    """
    Performs a simple selection sort of the list of ranger records by expertise.
    :param records: the list of dictionaries to sort
    :return: a new sorted list
    """
    sorted_records = []
    full_length = len(records)
    while len(sorted_records) < full_length:
        lowest = records[0]
        for record in records:
            if record['expertise'] < lowest['expertise']:
                lowest = record
        sorted_records.append(lowest)
        records.remove(lowest)
    return sorted_records


# Main program.
window = create_gui()

# Read the rangers.txt file into a list of dictionaries called rangers.
rangers = []
file = open('rangers.txt', 'r', encoding='utf-8')
for line in file.readlines():
    values = line.strip().split('#')
    rangers.append({'first name': values[0],
                    'last name': values[1], 
                    'dob': values[2], 
                    'expertise': values[3], 
                    'employed': values[4]})    
file.close()

# Main GUI loop.
current_ranger = 0
while True:

    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break

    # Check for button presses.
    if event == '-PREVIOUS_BUTTON-':
        if current_ranger > 0:
            current_ranger -= 1
    if event == '-NEXT_BUTTON-':
        if current_ranger < len(rangers) - 1:
            current_ranger += 1
    if event == 'Search':
        target = perform_search(rangers, values['-SEARCH_TEXTBOX-'])
        if target == -1:
            sg.popup('The text could not be found.', no_titlebar=True)
        else:
            current_ranger = target
    if event == 'Sort by last name':
        rangers = sort_by_last_name(rangers)
        current_ranger = 0
    if event == 'Sort by expertise':
        rangers = sort_by_expertise(rangers)
        current_ranger = 0

    # Update the record display.
    window['-FIRST_NAME_LABEL-'].update(rangers[current_ranger]['first name'])
    window['-LAST_NAME_LABEL-'].update(rangers[current_ranger]['last name'])
    window['-DOB_LABEL-'].update(rangers[current_ranger]['dob'])
    window['-EXPERTISE_LABEL-'].update(rangers[current_ranger]['expertise'])
    window['-EMPLOYED_LABEL-'].update(rangers[current_ranger]['employed'])
    window['-INDEX_LABEL-'].update(current_ranger + 1)
    if current_ranger == 0:
        window['-PREVIOUS_BUTTON-'].update(disabled=True)
    else:
        window['-PREVIOUS_BUTTON-'].update(disabled=False)
    if current_ranger == len(rangers) - 1:
        window['-NEXT_BUTTON-'].update(disabled=True)
    else:
        window['-NEXT_BUTTON-'].update(disabled=False)

window.close()
