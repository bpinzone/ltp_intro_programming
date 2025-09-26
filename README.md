# LTP - Intro to Programming

## Download and Installation
0. Download this pdf to make the links clickable.
1. Download and install Visual Studio Code ("VS Code")
    - [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

2. Download the code. (This will download a zip file)
    - [https://github.com/bpinzone/ltp_intro_programming/archive/refs/heads/main.zip](https://github.com/bpinzone/ltp_intro_programming/archive/refs/heads/main.zip)

3. Unzip the downloaded .zip file that contains the code.
    - Mac: double click
    - Windows: Right click -> Extract all

## Opening VS Code
4. Open the vscode app
    - Then click File -> Open Folder -> Open the folder you just unzipped.
    - Be sure to open the folder that contains all the files. Not a folder that contains a folder containing the files...


5. On the left side you should see a list of files. Open "life_logic.py" by double clicking it.
    - This is the code you'll be editing later. But first lets try to run it.

## Making sure we have the python programming language
6. Click View -> Terminal
    - This opens up a new window on the bottom that we can type commands into.

7. Type the command `python --version` and hit enter. (note that is 2 dash characters)
    - You should see "Python" followed by a version number. Not something like "command not found."
    - If you do not, try "python3 --version"
    - If you still do not, you're likely on windows. Download the Python app from the Microsoft Store app. Any of Python 3.13, 3.12, etc will be fine. Then RESTART vscode! (And open the folder again if it doesn't automatically).

## Installing pygame

8. Next we make sure we have a package manager.
    - You may need to use "python" or "python3" in the below command depending what worked for you above.
    - In the Terminal enter the command `python -m ensurepip --upgrade`

9. Install pygame. You may need to use "pip" or "pip3"
    - Enter the command `pip install -r requirements.txt`

## Running our program
10. Again, maybe type python or python3 depending on above.
- Enter the command `python life_logic.py`
- You should see a new window pop up. Try clicking on a few of the cells, then hitting Play
