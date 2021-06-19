from tkinter import *
import sys
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
from pynput import keyboard

class QuitMe(Frame):                        
    def __init__(self, parent=None):          
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)
    def quit(self):
        ans = messagebox.askokcancel('Confirm exit', "Sure you want to Quit?")
        if ans: Frame.quit(self)
def onSave(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            alltext = self.gettext()                      
            open(filename, 'w').write(alltext)          
class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)               
        self.makewidgets()
        self.settext(text, file)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN , font=("iransansdn",10),bg="red")
        sbar.config(command=text.yview)                  
        text.config(yscrollcommand=sbar.set)           
        sbar.pack(side=RIGHT, fill=Y)                   
        text.pack(side=LEFT, expand=YES, fill=BOTH)     
        self.text = text
    def settext(self, text='', file=None):
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                   
        self.text.insert('1.0', text)                  
        self.text.mark_set(INSERT, '1.0')              
        self.text.focus()                                
    def gettext(self):                               
        return self.text.get('1.0', END+'-1c')         


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())
class SimpleEditor(ScrolledText):                        
    def __init__(self, parent=None, file=None):
        def open_text_file():
                    #self.text.
                    filetypes = (
                             ('text files', '*.txt'),
                             ('All files', '*.*')
                              )
    # show the open file dialog
                    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
                    self.text.insert('1.0', f.read())
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Open',  command=open_text_file).pack(side=LEFT)
        Button(frm, text='Save',  command=self.onSave).pack(side=LEFT)
        Button(frm, text='Cut',   command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        #Button(frm, text='Find',  command=self.onFind).pack(side=LEFT)
        QuitMe(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file) 
        self.text.config(font=("iransans",10))
    def onSave(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            alltext = self.gettext()                      
            open(filename, 'w').write(alltext)          
    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)        
        self.text.delete(SEL_FIRST, SEL_LAST)           
        self.clipboard_clear()              
        self.clipboard_append(text)
    def onPaste(self):                                    
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass                                      

#if there are no cmdline arguments, open a new file. 
if len(sys.argv) > 1:
	SimpleEditor(file=sys.argv[1]).mainloop()                
else:
	SimpleEditor().mainloop()
