def getDarkTheme():
    return """
    #centralwidget {background-color: #333333;}
#Sub1, #menu, #q1_header, #q2_header,#new_2,#new_3,#container_3,#new_4,#name_widget_3,#name_widget,#widget_4,#widget_11,#widget_12,#widget_15,#widget_17,#widget_18,#stitle4,#stitle5{
border-radius: 15px;
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #292929, stop: 1 #1a1a1a);
color: #FFFFFF;
border: 1px solid #555555;}
#qn_1, #qn_2 {
border-radius: 15px;
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #444444, stop: 1 #333333);
color: #CCCCCC;
border: 1px solid #555555;
}
#container_4
{
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);
border-radius: 15px;
}
QScrollArea {
border-radius: 20px;
border: 1px solid #555555;
 }
QScrollArea > QWidget > QWidget {
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);
border-radius: 15px;
}
QPushButton {
border: 2px solid transparent; 
border-radius: 10px;
background-color: rgba(0, 0, 0, 0.5);
padding: 10px 20px;
font-size: 16px;
font-weight: bold;
color: white;
border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);
}
QPushButton:hover {
background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);
color: black;
border: 2px solid transparent; 
border-color: black; 
}
QLabel {
color: #CCCCCC;}
QPlainTextEdit {
background-color: #333333;
color: #CCCCCC;
border: 1px solid #555555;
border-radius: 10px;
padding: 5px;
}
QComboBox {
background-color: #333333;
color: #CCCCCC;
border: 1px solid #555555;
border-radius: 10px;
padding: 5px;
}
QComboBox QAbstractItemView {
background-color: #333333; 
color: #FFFFFF; 
border: 1px solid #29a19c;
selection-background-color: #29a19c;
selection-color: #1e1e1e;
}
QTabWidget::pane {
border-radius: 15px;
border: 1px solid #555555;
}
QTabBar::tab {
border: 2px solid transparent; 
border-radius: 10px;
background-color: rgba(0, 0, 0, 0.5);
padding: 10px 20px;
font-size: 16px;
font-weight: bold;
color: white;
border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);
}
QTabBar::tab:hover {
background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);
color: black;
border: 2px solid transparent; 
border-color: red;
 }
QTabBar::tab:selected {
background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);
color: black;
border: 2px solid transparent; 
border-color: black;
 }

#stud_home,#stud_profile,#widget_19,#Box,#widget_20
{
border-radius: 15px;
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);
color: #FFFFFF;
border: 1px solid #555555;
padding: 20px;}

QLabel {
    color: white;
}

QLineEdit {
    border: none;
    border-radius: 10px;
    background-color: #3A3A3A; /* Dark Grey */
    color: #FFFFFF;
    padding: 10px;
}

QLineEdit:focus {
    background-color: #1C1C1C; /* Light Grey */
}

"""

def getLightTheme():
    return """
    #centralwidget {background-color:  rgb(234, 234, 234);}
#Sub1, #menu, #q1_header, #q2_header,#new_2,#new_3,#container_3,#new_4,#name_widget_3,#name_widget,#widget_4,#widget_11,#widget_12,#widget_15,#widget_17,#widget_18,#stitle4,#stitle5{
border-radius: 15px;
background-color: qlineargradient(
    x1: 0, y1: 0, x2: 1, y2: 1,
    stop: 0 #d0d0d0, stop: 1 #c6c6c6
);
color: #000000;
border: 1px solid #aaaaaa;}
#qn_1, #qn_2 {
border-radius: 15px;
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #cccccc, stop: 1 #bbbbbb);
color: #333333;
border: 1px solid #aaaaaa;
}
#container_4
{
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #e1e5ea, stop: 0.3 #ccd1d9, stop: 1 #b8c2cc);
border-radius: 15px;
}
QScrollArea {
border-radius: 20px;
border: 1px solid #aaaaaa;
}
QScrollArea > QWidget > QWidget {
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #e1e5ea, stop: 0.3 #ccd1d9, stop: 1 #b8c2cc);
border-radius: 15px;
}
QPushButton {
border: 2px solid transparent;
border-radius: 10px;
background-color: rgba(0, 0, 0,0.25);
padding: 10px 20px;
font-size: 16px;
font-weight: bold;
color: black;
border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 0.3 #29a19c, stop: 1 #2ecc71);
}
QPushButton:hover {
background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 0.3 #29a19c, stop: 1 #2ecc71);
color: white;
border: 2px solid transparent;
border-color: white;
}
QLabel {
color: #333333;}
QPlainTextEdit {
background-color: #f5f5f5;
color: #333333;
border: 1px solid #aaaaaa;
border-radius: 10px;
padding: 5px;
}
QComboBox {
background-color: #f5f5f5;
color: #333333;
border: 1px solid #aaaaaa;
border-radius: 10px;
padding: 5px;
}
QComboBox QAbstractItemView {
background-color: #f5f5f5;
color: #000000;
border: 1px solid #29a19c;
selection-background-color: #29a19c;
selection-color: #f5f5f5;
}
QTabWidget::pane {
border-radius: 15px;
border: 1px solid #aaaaaa;
}
QTabBar::tab {
border: 2px solid transparent;
border-radius: 10px;
background-color: rgba(255, 255, 255, 0.5);
padding: 10px 20px;
font-size: 16px;
font-weight: bold;
color: black;
border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 0.3 #29a19c, stop: 1 #2ecc71);
}
QTabBar::tab:hover {
background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 0.3 #29a19c, stop: 1 #2ecc71);
color: white;
border: 2px solid transparent;
border-color: red;
}
QTabBar::tab:selected {
background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 0.3 #29a19c, stop: 1 #2ecc71);
color: white;
border: 2px solid transparent;
border-color: white;
}

#stud_home,#stud_profile,#widget_19,#Box,#widget_20
{
border-radius: 15px;
background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #e1e5ea, stop: 0.3 #ccd1d9, stop: 1 #b8c2cc);
color: #000000;
border: 1px solid #aaaaaa;
padding: 20px;}

QLabel {
color: black;
}

QLineEdit {
border: none;
border-radius: 10px;
background-color: #ffffff;
color: #000000;
padding: 10px;
}

QLineEdit:focus {
background-color: rgba(0, 0, 0,0.25);
}

"""
