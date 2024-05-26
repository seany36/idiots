from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from PyQt5.QtGui import QFont, QColor, QPalette
from random import shuffle, randint

# ----------------------------------------------------------
# The widgets and mockups have been created. Next, the functions: 
# ----------------------------------------------------------

class Question():
    ''' contains the question, one correct answer and three incorrect answers'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # all the lines must be given when creating the object, and will be recorded as properties
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# -------------------------------------------------------------
# Create a question banks
# -------------------------------------------------------------
questions_list = [] 
questions_list.append(Question('What is the capital of Australia?', 'Canberra', 'Sydney', 'Melbourne', 'Brisbane'))
questions_list.append(Question('Who painted the famous Mona Lisa?', 'Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet'))
questions_list.append(Question('Which ocean is the largest in the world?', 'Pacific Ocean', 'Arctic Ocean', 'Atlantic Ocean', 'Indian Ocean'))
questions_list.append(Question('Who wrote the play "Romeo and Juliet"?', 'William Shakespeare', 'Mark Twain', 'Charles Dickens', 'Jane Austen'))
questions_list.append(Question('What is the currency of Japan?', 'Yen', 'Euro', 'Dollar', 'Pound'))
questions_list.append(Question('In which country would you find the Great Barrier Reef??', 'Australia', 'United Kingdom', 'Canada', 'New Zealand'))
questions_list.append(Question('Who is known as the "Father of Geometry"?', 'Euclid', 'Archimedes', 'Pythagoras', 'Aristotle'))
questions_list.append(Question('What is the chemical symbol for gold?', 'Au', 'Ag', 'G', 'Go'))
questions_list.append(Question('Which continent is the driest in the world?', 'Antartica', 'Australia', 'Africa', 'Europe'))
questions_list.append(Question('Which ocean is the largest in the world?', 'Jupiter', 'Saturn', 'Neptune', 'Sun'))

# Creating window and application -------------------------------
app = QApplication([])
# Set the application style
app.setStyle('Fushion')  # Windows, Fusion, Breeze, QtCurve, Oxygen

# Set the application font
font = QFont("Calibiri", 12)
app.setFont(font)

# Set the application color palette
palette = QPalette()
palette.setColor(QPalette.Window, QColor(255, 255, 255))  # Set the background color
palette.setColor(QPalette.WindowText, QColor(0, 0, 0))      # Set the text color
app.setPalette(palette)

window = QWidget()
window.setWindowTitle('Memory Card')

width = 600
height = 300
window.resize(width, height)

# Create Widgets ------------------------------------------------
## Create question panel
lb_Question = QLabel('Questions here')
btn_OK = QPushButton('Answer') # NextQuetion

## Create answer box
RadioGroupBox = QGroupBox("Answer Options:") # put them into a greyed out box
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

# Group all the buttons 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Set the font for specific widgets
lb_Question.setFont(QFont("Calibiri", 14))  # Set font for the question label
# lb_Result.setFont(QFont("Arial", 14))     # Set font for the result label
# lb_Correct.setFont(QFont("Arial", 14))    # Set font for the correct answer label
# btn_OK.setFont(QFont("Arial", 12))         # Set font for the OK button

# # Set colors for specific widgets
# lb_Result.setStyleSheet("color: red;")     # Set the result label color to red
# lb_Correct.setStyleSheet("color: green;")  # Set the correct answer label color to green


# Create an answer panel layout --------------------------
layout_answer = QHBoxLayout()   
layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans1.addWidget(rbtn_1) # two answers in the first column
layout_ans1.addWidget(rbtn_2)
layout_ans2.addWidget(rbtn_3) # two answers in the second column
layout_ans2.addWidget(rbtn_4)

layout_answer.addLayout(layout_ans1)
layout_answer.addLayout(layout_ans2)
RadioGroupBox.setLayout(layout_answer)

# Create a results panel ------------------------------
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('You are correct/ You are incorrect!') # “Correct” or “Incorrect” text will be here
lb_Correct = QLabel('The correct answer will be here!') # correct answer text will be written here 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Main Layout ---------------------------------------
# Place all the widgets in the window:
layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result
layout_line3 = QHBoxLayout() # “Answer” button

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Put both panels in the same line; one of them will be hidden and the other will be shown:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() #Hide the answer panel

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large
layout_line3.addStretch(1)

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=6)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between content

window.setLayout(layout_card)

# ----------------------------------------------------------
# The widgets and mockups have been created. Next, the functions: 
# ----------------------------------------------------------

def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')

    RadioGroup.setExclusive(False) # to reset radio button selection
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # bring back the limits so only one radio button can be selected 

# def test():
#     ''' a temporary function '''
#     if 'Answer' == btn_OK.text():
#         show_result()
#     else:
#         show_question()

# Functions (set 2) ---------------------------------------------------
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    ''' the function writes the value of the question and answers 
    into the corresponding widgets while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        show_correct('You are correct!')
        window.score += 1
        print('Statistics\n-Total questions: ', window.cur_question +1, '\n-Right answers: ', window.score)
        print(f'Rating: {window.score/(window.cur_question+1)*100}%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('You are incorrect! \nThe correct answer is:')
            print('Statistics\n-Total questions: ', window.cur_question +1, '\n-Right answers: ', window.score)
            print('Rating: ', (window.score/(window.cur_question+1)*100), '%')

def next_question():
    ''' Asks the next question in the list. '''
    # this function needs a variable that gives the number of the current question 
    # this variable can be made global, or it can be the property of a “global object” (app or window)
    # we will create the property window.cur_question (below)
    window.cur_question = window.cur_question + 1 # move on to the next question 
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # if the list of questions has ended, start over 
        window.score =0
    q = questions_list[window.cur_question] # take a question
    ask(q) # ask it

def click_OK():
    ''' This determines whether to show another question or check the answer to this question. '''
    if btn_OK.text() == 'Answer':
        check_answer() # check the answer
    else:
        next_question() # next question

# Event procesing ----------------------------------------------
# btn_OK.clicked.connect(test) # check that the answer panel appears when the button is pressed
window.score = 0
window.total = 0
window.cur_question = -1
# q = Question('Select the most appropriate English name for the programming concept to store some data', 'variable', 'variation', 'variant', 'changing')
# ask(q)

# ask('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')
# btn_OK.clicked.connect(check_answer)

btn_OK.clicked.connect(click_OK) # when a button is clicked, we choose what exactly happens 
# Everything is set up. Now we ask the question and show the window:
next_question()


# Window application run --------------------------
window.show()
app.exec_()