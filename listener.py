import keyboard

def print_event(e):
    print(e.name, e.event_type, e.scan_code)

keyboard.hook(print_event)
print("Listening for keyboard events... Press ESC to stop.")
keyboard.wait('esc')
