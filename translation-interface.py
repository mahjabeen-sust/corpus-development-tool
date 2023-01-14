# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:25:26 2018

@author: Asus
"""

import sys
from PyQt5 import QtWidgets, uic
 
qtCreatorFile = "pyqt5-interface.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.input_file=""                
        self.en_sentences=[]        
        self.counter=0
        self.skipped_index=[]
        self.counter_file_name=""
        self.counter_fin=""
        self.skip_file_name=""
        #self.load_source_sentence()
        #self.translateButton.clicked.connect(self.translate)
        self.translateButton.clicked.connect(self.validate_target_line)
        #self.exitButton.clicked.connect(self.close)
        self.skipButton.clicked.connect(self.manage_skip)
        self.openButton.triggered.connect(self.openbutton_triggered) 
    
    def translate(self):
        src=self.source.text()
        translated = self.target.text()
        text=src+"\t"+translated
        #print(text.encode('utf-8'))
        out_file=self.input_file.replace(".txt","_translated.txt")
        fout=open(out_file,'a+',encoding='utf-8')        
        fout.write(text)
        fout.write('\n')
        fout.close()
        counter_fin=open(self.counter_file_name,'w+',encoding='utf-8')
        counter_fin.write(str(self.counter))
        counter_fin.close()
        self.load_source_sentence()
        
    def load_source_sentence(self):
        if self.input_file=="":
            self.line_validate.setText("")
        else:
            #counter_fin=open('counter.txt','r',encoding='utf-8')
            self.is_counter_file_exist()
            line_writen=""
            for line in self.counter_fin:
                line_writen=line.rstrip()
            self.counter_fin.close()
            #if no translation is done, start from the beginning, else start from next to the last translation
            if line_writen=="":
                self.counter=0
            else:
                self.counter=int(line_writen)        
            
            if self.counter<len(self.en_sentences):
                src=self.en_sentences[self.counter]                  
                self.source.setText(src)
            if self.counter>=len(self.en_sentences):
                self.source.setText("")            
                self.line_validate.setText("Translation task is complete !!")
            self.target.setText("")
            self.counter=self.counter+1  
        
    def validate_target_line(self):
        test=self.target.text()
        if test=="":
            self.line_validate.setText("Translation Field is Empty !!")            
        else:
            self.line_validate.setText("")   
            self.translate()
            
    def manage_skip(self):
        if self.input_file=="":
            self.line_validate.setText("No sentence to skip !!")
        else:
            self.skipped_index.append(self.counter-1)
            self.skip_file_name=self.input_file.replace(".txt","_skipped.txt")
            skip_out=open(self.skip_file_name,'a+',encoding='utf-8')
            skip_out.write(self.en_sentences[self.counter-1])
            skip_out.write('\n')
            skip_out.close()
            counter_fin=open(self.counter_file_name,'w+',encoding='utf-8')
            counter_fin.write(str(self.counter))
            counter_fin.close()
            self.counter=self.counter+1
            self.line_validate.setText("")  
            self.load_source_sentence()
            #write in another file?
        
    def openbutton_triggered(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            self.line_validate.setText("")
            #print(fileName)
            self.input_file=fileName
            self.counter_file_name=fileName.replace(".txt","_counter.txt")
            #print(self.counter_file_name)
            self.load_input_file()
        else:
            self.line_validate.setText("Choose a file to translate !!")
	
    def load_input_file(self):
        fin=open(self.input_file,'r',encoding='utf-8')
        for lines in fin:
            self.en_sentences.append(lines.rstrip())
        fin.close()
        self.load_source_sentence()
    
    def is_counter_file_exist(self):
        try:
           self.counter_fin=open(self.counter_file_name,"r",encoding='utf-8')
        except IOError: 
           out_counter=open(self.counter_file_name,'w+',encoding='utf-8')
           out_counter.write(str(0))
           out_counter.close()
           self.counter_fin=open(self.counter_file_name,"r",encoding='utf-8')
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    