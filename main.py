import ctypes
import keyboard
import multiprocessing
import time

# Constants for monitor power states and SendMessage parameters
MONITOR_OFF = 2
MONITOR_ON = -1
SC_MONITORPOWER = 0xF170
HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112

def monitor_control_worker(state):
    """Worker function to change the monitor's power state."""
    try:
        ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, state)
        print(f"Monitor state set to {'on' if state == MONITOR_ON else 'off'}.")
    except Exception as e:
        print(f"Failed to set monitor state: {e}")

def set_monitor_power_state_with_timeout(state, timeout=25):
    """Attempts to set the monitor power state with a timeout."""
    print(f"Attempting to turn monitors {'on' if state == MONITOR_ON else 'off'}...")
    process = multiprocessing.Process(target=monitor_control_worker, args=(state,))
    process.start()
    process.join(timeout)
    if process.is_alive():
        print("Operation timed out, attempting to terminate...")
        process.terminate()
        process.join()

def turn_monitors_on():
    set_monitor_power_state_with_timeout(MONITOR_ON)

def turn_monitors_off():
    set_monitor_power_state_with_timeout(MONITOR_OFF)

def exit_script():
    """Exits the script."""
    print("Exiting script...")
    exit(0)

def register_hotkeys():
    keyboard.add_hotkey('alt+y', turn_monitors_on)
    keyboard.add_hotkey('alt+n', turn_monitors_off)
    keyboard.add_hotkey('esc+o', exit_script)

    print("Script running... Press Alt+Y to turn monitors on, Alt+N to turn them off, and ESC to exit.")
    keyboard.wait('esc')

if __name__ == '__main__':
    # This is crucial for multiprocessing to work correctly on Windows.
    multiprocessing.freeze_support()
    register_hotkeys()
