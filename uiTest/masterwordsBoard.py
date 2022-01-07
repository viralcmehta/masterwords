from typing import SupportsAbs
from pyforms.gui.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlLabel, ControlEmptyWidget


class Attempt(BaseWidget):
    def __init__(self, _value):
        value = _value
    
        c0 = ControlLabel(value[0])
        c1 = ControlLabel(value[1])
        c2 = ControlLabel(value[2])
        c3 = ControlLabel(value[3])
        c4 = ControlLabel(value[4])

        empty = ControlEmptyWidget();
        empty.value = [c0,c1,c2,c3,c4]

        c0.value = "W"
        c1.value = "O"
        c2.value = "R"
        c3.value = "L"
        c4.value = "D"



class BoardWindow(BaseWidget):
    def __init__(self, _numAttempts=5):
        super(BoardWindow,self).__init__('Master Word Board')

        numAttempts = _numAttempts
        self.c00 = ControlLabel("*")
        self.c01 = ControlLabel("*")
        self.c02 = ControlLabel("*")
        self.c03 = ControlLabel("*")
        self.c04 = ControlLabel("*")

        self.c10 = ControlLabel("*")
        self.c11 = ControlLabel("*")
        self.c12 = ControlLabel("*")
        self.c13 = ControlLabel("*")
        self.c14 = ControlLabel("*")

        self.c20 = ControlLabel("*")
        self.c21 = ControlLabel("*")
        self.c22 = ControlLabel("*")
        self.c23 = ControlLabel("*")
        self.c24 = ControlLabel("*")

        self.c30 = ControlLabel("*")
        self.c31 = ControlLabel("*")
        self.c32 = ControlLabel("*")
        self.c33 = ControlLabel("*")
        self.c34 = ControlLabel("*")

        self.c40 = ControlLabel("*")
        self.c41 = ControlLabel("*")
        self.c42 = ControlLabel("*")
        self.c43 = ControlLabel("*")
        self.c44 = ControlLabel("*")

        self.nextAttempt = 0
        self.maxAttempt = 4

        self.attempts = [
            [self.c00, self.c01, self.c02, self.c03, self.c04],
            [self.c10, self.c11, self.c12, self.c13, self.c14],
            [self.c20, self.c21, self.c22, self.c23, self.c24],
            [self.c30, self.c31, self.c32, self.c33, self.c34],
            [self.c40, self.c41, self.c42, self.c43, self.c44]
        ]

        self.entryBox = ControlText("try your luck", "default")
        self.submitBtn = ControlButton("Submit")
        self.submitBtn.value = self.SubmitBtnClick

        form = [ 
            ("c00", "c01", "c02", "c03", "c04" ),
            ("c10", "c11", "c12", "c13", "c14" ),
            ("c20", "c21", "c22", "c23", "c24" ),
            ("c30", "c31", "c32", "c33", "c34" ),
            ("c40", "c41", "c42", "c43", "c44" ),
            "=",
            ('entryBox', 'submitBtn')
        ]
        self.formset = form            

    def SubmitNextAttempt(self, str):
        if(self.nextAttempt > self.maxAttempt): 
            return

        lblList = self.attempts[self.nextAttempt]

        for i in range(len(lblList)):
            lblList[i].value = str[i]

        self.nextAttempt += 1


    def SubmitBtnClick(self):
        textEntered = self.entryBox.value
        print("TextEntered: " + textEntered)
        self.SubmitNextAttempt(textEntered)


if __name__ == "__main__":  
    from pyforms import start_app
    start_app( BoardWindow )