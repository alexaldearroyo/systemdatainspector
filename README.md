# System Data Inspector

![Static Badge](https://img.shields.io/badge/Made%20with-Python%203-brightgreen)

The System Data Inspector for MacOS provides a quick and efficient way to view the approximate calculations of potentially modifiable space occupied by System Data on your Mac. With it, you can view various directories and their sizes.

![Screenshot](Resources/screenshot1.png)

## Requirements

- MacOS Operating System
- Python 3.x

## Permissions

**Important:** For the program to function correctly, it needs access to the Mac's hard drive.

### Granting Disk Access

To ensure the MacOS System Data Inspector works correctly:

1. Open **System Settings**.
2. Click on **Privacy & Security**.
3. Scroll down and select **Full Disk Access** on the left side.
4. Unlock the settings of the program where you are going to execute the script (usually "Terminal") by clicking the lock icon at the bottom left and entering your password.
5. You may need to restart the Python application or the terminal for the changes to take effect.

## Usage

To run the System Data Inspector in the terminal:

```bash
python3 <path_to_script>/systemdatainspector.py
```

Follow the on-screen prompts to inspect the sizes of various directories and optionally delve deeper into specific directories.

## Features

- View total size for predefined system directories.
- Color-coded size display for better readability.
- Option to inspect individual directories in detail.
- Capability to open inspected directories in Finder.


Por supuesto, aquí tienes cómo podrías añadir una sección "Install and Execute as a Command" a tu archivo README.md, basándome en la explicación anterior y utilizando `sudo cp` en lugar de `sudo mv`:

## Install and Execute as a Command

To make the System Data Inspector easily executable from any directory using the command `sdi`, follow these steps:

### Make the Script Executable

Make your script executable by running:

```bash
chmod +x /path/to/systemdatainspector.py
```

### Copy the Script to a Directory in Your PATH

Copy the script to `/usr/local/bin` and rename it as `sdi`:

```bash
sudo cp /path/to/systemdatainspector.py /usr/local/bin/sdi
```

### Execution

After these steps, you can run the System Data Inspector from any directory simply by typing:

```bash
sdi
```

This will execute the `systemdatainspector.py` script.

Remember to replace `/path/to/systemdatainspector.py` with the actual path to your script.

## Credits

&copy; Alex Arroyo, 2023