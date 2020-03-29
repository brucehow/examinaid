# Useful Tips and Tricks

This file contains useful information in the event of a major change to the system.

## Creating a Python Virtual Environment and Installing Flask

These instructions assume a Windows 10 machine, and the **Visual Studio Code** development environement. Sections that relate directly to this environment will be noted as such. Before beginning, make sure your terminal window is in the project working directory, i.e. the directory in which you want to create a virtual environment. This should be the same directory in which your top level Python Flask file is located. Also ensure that you have **Python 3.8** installed. If you have an earlier version of Python, you may need to install a separate virtual environment initializer. You must use either **Windows Powershell** or **Git Bash** to run these commands; they are not guarenteed to work on the **Command Line** interface.

**IMPORTANT**: If you are cloning the repository to which this file belongs to for the first time, you will need to create a virtual environment within the workspace at the root directory of the repository. **Git will not track the files or packages within the virtual environment on your machine**; it is your responsibility to keep these up to date.

The first 3 steps may need to be run if the previous virtual environment is not recognized. If this is the case, remove the previous virtual environment and rerun these steps.

(Windows)
1. In the terminal window, double check that the working directory is correct, then call `python -m venv venv`. The second `venv` is the name that you wish to give your virtual environment. For the purposes of this repository and to ensure that Git does not track the virtual environment, you must use the name `venv` within this workspace.
2. Once the virtual environment has been set up, in the same directory, type `source venv/Scripts/activate` to activate the virtual environment, again replacing the `venv` with the name of your virtual environment, if different. Upon successful completion, you can check that the virtual environment has been set up by calling `ls`. The last output of that command should be `(venv)`. This command needs to be called every time a new terminal instance is created.

(Mac)
1. If you are having issues with the above steps try this. Call `virtualenv venv -p 3.8`.
2. Then activate the environment using `source venv/bin/activate`.

3. In the same directory, call `pip install flask`. This installs several dependencies alongside Flask.

If your editor of choice is Visual Studio Code, you now have to change the python interpreter in the workspace. This is done to avoid meaningless error messages due to the new virtual environment not being initially recognized. Steps 4 - 6 address this; skip these steps if they don't apply to you.

4. Hit "Ctrl + ," to open the settings, and select the Workspace tab.
5. Search for "pythonPath" in the search bar at the top and navigate down to the section titled "Python: Python Path".
6. Add the corresponding path to the Python executable in the virtual environment to the python interpreter in this section.

Back to the terminal, we now need to give the Flask application to the environmental variable.

7. Still in the same directory, once your Flask application is ready to be run, call `set FLASK_APP=index.py`, where `index.py` is the top level python script to run your Flask application. We need to pass the top level script to the environmental variable so it knows what script to look for when we call the function in the next step.
8. Your application should be ready to be served to a local address! Call `flask run` and navigate to the given address to see the app in action.
