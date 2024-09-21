# Timecode Exporter

An utility to export timecodes from a Sequence in Premiere or a Timeline in DaVinci Resolve.

## Usage with Premiere

```
We need to export the Sequence first. After editing, open Premiere and select the Sequence

Go to File → Export → EDL...
(This is a file format with timecode data.)

You can leave the default options and click ok. Save the file whereever you'd like

Open Timecode Exporter. Drag and drop the .edl file

The timecodes are display and automatically copied to your clipboard
```

## Usage with DaVinci Resolve

```
We need to export the Timeline first. After editing, open Resolve and select the Timeline

Go to File → Export → Timeline...
(This is a file format with timecode data.)

Export as EDL files. Save the file whereever you'd like

Open Timecode Exporter. Drag and drop the .edl file

The timecodes are display and automatically copied to your clipboard
```

## Development (Windows)

```
The app is based on a python script.

conda create -n timecode_exporter python=3.9
conda activate timecode_exporter

conda install pyperclip tk
pip install tkdnd

cd /D C:\\Timecode-Exporter\Windows

pyinstaller --onefile --windowed --icon=timecode_exporter.ico --add-data "timecode_exporter.ico;." --add-data "C:\Users\ABC\miniconda3\envs\timecode_exporter\Lib\site-packages\tkinterdnd2\tkdnd\win-x64;TkinterDnD2" "C:\\Timecode-Exporter\Windows\timecode_exporter.py"

The icon is exported using [icoconverter.com](https://www.icoconverter.com/)
```

## Development (MacOS)

```
The app is based on a bash script and created with the droplet option in Platypus.

The icon is exported using [Adobe Illustrator .icns exporter](https://github.com/choffmeister/adobe-illustrator-icnsexport)

ln -s /Applications /Users/ABC/Downloads/Timecode\ Exporter/MacOS/dmg/Copy\ to\ Applications

(cd /Users/ABC/Documents/Timecode\ Exporter/Release/Timecode\ Exporter\ v1.0.0/For\ MacOS && zip -r ../out.zip .)
```

## Development (MacOS)

```

Python version:
pyinstaller --onefile --windowed --add-data "timecode_exporter.icns:." --add-data "/opt/miniconda3/envs/timecode_exporter/lib/python3.9/site-packages/tkinterdnd2/tkdnd/osx-arm64:TkinterDnD2" --icon=timecode_exporter.icns timecode_exporter.py

pyinstaller --onefile --windowed --add-data "timecode_exporter.icns:." --add-data "/opt/miniconda3/envs/timecode_exporter/lib/python3.9/site-packages/tkinterdnd2/tkdnd/osx-x64:TkinterDnD2" --icon=timecode_exporter.icns timecode_exporter.py


pip install tkinterdnd2 pyperclip tk
```
