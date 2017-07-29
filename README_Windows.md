# News Reader for Windows

## It extracts news from all sources of your interest and speaks out the headline. It also displays the headline along with link and descrition on terminal, so that you can explore further. 

# Requirements
* Python 3 (Tested on Python 3.5)
* Pyttsx3 (install using ```pip install pyttsx3```)
* Progressbar (install using ```pip install progressbar```)

**NOTE:** If errors occur during progressbar installation, download .whl file for progressbar from Christoph Gohlke's Repository of Windows Binaries for Python at http://www.lfd.uci.edu/~gohlke/pythonlibs/
Install using ```pip install <PATH-TO-FILE>```

# Usage
* Register yourself at https://newsapi.org/register and generate your API-key
* Run setup_system.py from command line using ```python setup_system.py``` and follow the instructions. This needs to be done once during setup.
* Run NewsReader.py from command line by entering ```python NewsReader.py``` to listen to news updates. 
