## Corpus Development Tool

## Introduction
A simple Natural Language Processing tool for multipurpose application.
The primary objective of this project is to provide a user interface to manually develop any text corpus (translation by human translator). Machine translation system requires training data in text format. The conventional format for a text corpus is a tab-seperated text file where the source and target sentences are stored along with a tab (white space). This application gives user flexibility to choose any pair of languages as the source and target data. The user can skip any number of source data if they do want to translate them at that moment. The skipped data is stored in seperate files, and user can reuse them again as source data. 


## Project Setup
You need to install the dependecies for the project like Pyhton, PyQt5.

### Cloning the git repo
The code for this project is located on github at the following URL 
[corpus-development-tool](https://github.com/mahjabeen-sust/corpus-development-tool)

In order to clone it into your project, you can simply type the following command from the folder where you would like to install the project.

`git clone https://github.com/mahjabeen-sust/corpus-development-tool`


## The Application

This project is built with python. It is a simple user interface that prompts user to provide translation for a source sentence one at a time. User can use any two languages as their source and target data. The sources sentences (The one you want to translate) can be present in a simple text file. The application will create the output text file in a tab-seperated format with both source and target (translated) sentecne.

### To install python and associated dependencies.

Here is the command-line method to install the dependencies for this project.  You need python and PyQt5 for the application. To install python for your computer, go to the following website:
```
https://www.python.org/downloads/
```
Download the appropriate version of python for your computer and run the installer. Once you have installed the python, open the command prompt (terminal) and run the following command
```
pip install PyQt5
```

### Running the application


In order to run this from the command line just type...

```
python translation-interface.py
```
Once the interface is opened, you can choose your source (input) file from the File-->Open menu. Then, the application will present you the source sentences one by one. You have to type the translation for the source data and click 'Submit Translation' button. These source and target pair will be saved into another text file, and the next source data will appear automatically. There is 'Skip' button that will allow you to skip any particular sentecne that you might not want to translate at that moment, and bring you another sentecne to translate instead. These skipped sentences are stored in another file with the extension '_skipped.txt', so you can invoke them for translation later.
When you finish translating your whole source file, the application will inform you!
Happy Corpusing...!



