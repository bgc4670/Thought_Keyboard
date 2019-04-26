# Thought_Keyboard
Type with your mind!

A project with NXT (Neurotechnology Exploration Team), an all-undergraduate research team at RIT (Project Lead: Forest).

The goal of this project is to give people with mobility disabilities the ability to easily use computers.
This is done with a dry EEG (ElectroEncephaloGram) ran through a BCI (Brain Control Interface) that translates the brainwaves in computer readable signals. This is translated through a Pylsl program (incomplete) into the Python Thought_Keyboard program.
The main libraries used are PyQT and pyautogui.

Currently there are numerous issues with the program. The window needs to be made so that it does not refresh with every button press. Then, the addition of key to mouse functionality to move the cursor with digital inputs needs implimented. The actual layout needs to be vision-impaired friendly as far as color and font size and such. The creation of the pylsl program and integration to the BCI via the pylsl program will come later. More human testing with input (probably involoving machine learning algorithms and developing "typing games" for proficiency) with happen simultainious to the funtional programing.

To be able to complete the program up to this point, I had to learn a bit of C++ to translate QT docs to PyQT. I also had to learn GUIs more completly, specifically in python. My python knowledge is little, although I could say that about any language. Preferably I would have used something object oriented, maybe a game maker such as Unity or even pygame. PyQT is necessary to ensure that the window is always on top of other windows, and the python language itself is most easily implimented with BCI.

The hardest part about this project thus far was certainly searching for relative code. As previously stated, there is not  any good formal  documentation for PyQT. Translating from C++ only got me so far, so German youtube videos and sketchy html sites were where I scoured. I have a few hours from just having incorrect syntax, like having parentheses on methods when they were noit necessary, or needing a speperat funtion to add parameters to those same functions.

Updates to this project will be fairly frequent as some for of working prototype wpuld be like for Imagine RIT.
