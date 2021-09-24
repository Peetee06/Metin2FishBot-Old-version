import PySimpleGUI as sg

class PyWindow:

    window = None

    def __init__(self):
        sg.theme('Dark Red')
        self.create_window()

    def bot_tab(self):
        return [[sg.Text('This bot works with OLD fishing mode.')],
                [sg.Frame('Bot stop conditions (ignore if infinite)', [
                    [sg.Checkbox('Total Time (Minutes)', key='-ENDTIMEP-'), sg.InputText(size=(5,10), key='-ENDTIME-')],
                    [sg.Text('Pull-Out time(2...3 recommended):'), sg.InputText(size=(5,10), key='-PULLTIME-')]
                    ])],
                [sg.Button('START', key='-BUTTONSTART-')]]

    def options_tab(self):
        return [[sg.Text('You can set the values of cooldowns.')],
                [sg.Frame('Time configuration', [
                    [sg.Text('Time in seconds')],
                   [sg.Text('Wait to put bait'),
                    sg.Slider(range=(2, 30), key="-BAITTIME-" , orientation='v', size=(5, 20), default_value=2),
                    sg.Text('Wait to throw'),
                    sg.Slider(range=(2, 30), key="-THROWTIME-", orientation='v', size=(5, 20), default_value=2),
                    sg.Text('Wait to start game'),
                    sg.Slider(range=(2, 5), key="-STARTGAME-", orientation='v', size=(5, 20), default_value=2),
                ]])]]

    def create_tabs(self):

        tab1_layout = self.bot_tab()
        tab2_layout = self.options_tab()

        tab_1 = sg.Tab('BOT', tab1_layout, font='Courier 15', key='-TAB1-')
        tab_2 = sg.Tab('OPTIONS', tab2_layout, font='Courier 15', key='-TAB2-')

        tab_group_layout = [[tab_1, tab_2]]

        return tab_group_layout

    def create_window_layout(self):

        tab_group_layout = self.create_tabs()

        return [[sg.TabGroup(tab_group_layout,
                 enable_events=True,
                 key='-TABGROUP-')]]

    def create_window(self):

        layout = self.create_window_layout()

        self.window = sg.Window('Metin2FishingBOT', layout, no_titlebar=False)
