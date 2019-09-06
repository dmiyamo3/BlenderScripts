# 3DTextMaker

This is a blender script that divides the input text for each character and outputs it as an FBX file.

# Requirement

 - blender2.8 β

# Usage

1. Start blender
1. Remove cube
1. Move to "Scripting" from the menu bar
1. Open `test.py`
1. Change dirname (output folder) and fontpath (font file) accordingly
1. Edit text freely
1. Change parameters freely (if you use bevel and remesh option, change isBevel and isRemesh from False to True respectively)
1. From the right-click menu, select “Run Script”
1. Text is split and generated in the specified folder as FBX file

# Example of Use

Example of import the output file to Unity

<img src="https://pbs.twimg.com/media/EDswQDxVAAAqY9G?format=jpg&name=large" width="480">

no option.

<img src="https://pbs.twimg.com/media/EDtQu6rU8AA1qsM?format=png&name=900x900" width="480">

bevel option.

<img src="https://pbs.twimg.com/media/EDtQu6rU0AE-BiL?format=png&name=900x900" width="480">

remesh option.

<img src="https://pbs.twimg.com/media/EDtQu6yUYAQm9HS?format=png&name=900x900" width="480">

bevel and remesh option.

<img src="https://pbs.twimg.com/media/EDtQu6xUEAAmPa3?format=png&name=900x900" width="480">