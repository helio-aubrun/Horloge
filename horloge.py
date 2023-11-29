import time

mode_12h = False
paused = False
alarm_time = None

def afficher_heure(heure):
    global current_time
    current_time = heure

def regler_alarme(heure):
    global alarm_time
    alarm_time = heure

def afficher_mode(mode):
    global mode_12h
    mode_12h = mode

def mettre_en_pause():
    global paused
    paused = True

def relancer():
    global paused
    paused = False

def afficher_heure_actuelle():
    global current_time
    global mode_12h

    if current_time is None:
        current_time = time.localtime()

    if paused:
        return

    heure = time.strftime("%H:%M:%S", current_time)

    if mode_12h:
        heure = time.strftime("%I:%M:%S %p", current_time)

    print(heure)

    if alarm_time is not None and alarm_time == time.localtime()[3:6]:
        print("ALARME !")

    current_time = time.localtime()

    time.sleep(1)
    afficher_heure_actuelle()

current_time = None

afficher_heure_actuelle()