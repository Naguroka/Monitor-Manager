# Monitor Manager

Monitor Manager is a Python-based tool designed to manage your computer monitors, allowing you to turn them off and on using hotkeys. This tool runs in the background and is perfect for users looking to have more control over their monitor power states without having to power them off manually.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To use Monitor Manager, you need:

- Python installed on your system (version 3.x is recommended).
- The `keyboard` and `ctypes` Python libraries. These can be installed via pip if not already installed:

```bash
pip install keyboard ctypes
```

### Installing

1. Clone the repository or download the ZIP file and extract it to a preferred location on your system.
2. Navigate to the project directory where `main.py` is located.

### Setting Up the Batch File for Startup

To ensure Monitor Manager starts automatically when you log into your computer:

1. Locate the `monitor_manager.bat` file within the project directory.
2. Edit the `monitor_manager.bat` file in a text editor and update the path to where `main.py` is located on your system. The file should contain the following line:

```batch
start /B pythonw "<absolute_path_to_your_script>\\main.py"
```

Replace `<absolute_path_to_your_script>` with the actual path to where `main.py` is located.

3. To have `monitor_manager.bat` run at startup:
   - Press `Win+R`, type `shell:startup`, and press Enter to open the Startup folder.
   - Copy or move `monitor_manager.bat` into this folder.

Alternatively, you can use Windows Task Scheduler to set up more specific conditions for when the script runs.

## Usage

Once set up, Monitor Manager will run silently in the background. Use the predefined hotkeys to control your monitors:

- `Alt+Y`: Turn monitors on.
- `Alt+N`: Turn monitors off.

## Built With

- [Python](https://www.python.org/) - The scripting language used.
- [keyboard](https://pypi.org/project/keyboard/) - For capturing hotkey presses.
- [ctypes](https://docs.python.org/3/library/ctypes.html) - For making system calls.

