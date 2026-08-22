# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# app = QApplication([])
# win = QWidget()

# win.move(500, 100)
# win.setFixedSize(500, 500)
# win.setGeometry(500,100,100,400)

# lbl_ism = QLabel("Ism: ", win)
# lbl_ism.move(0, 10)
# lbl_ism.setStyleSheet("background:lightgreen; font-size:30px")

# lbl_yosh = QLabel("Yosh: ", win)
# lbl_yosh.move(0, 50)
# lbl_yosh.setStyleSheet("background:red; color:white; font-size:30px; border:2px solid black")

# lbl_natija = QLabel("Yoshi:", win)
# lbl_natija.move(125, 110)
# lbl_natija.setStyleSheet("font-size: 30px")

# edit_ism = QLineEdit(win)
# edit_ism.move(100, 10)
# edit_ism.setStyleSheet("font-size: 25px")

# edit_yosh = QLineEdit(win)
# edit_yosh.move(120, 50)
# edit_yosh.setStyleSheet("font-size: 25px")

# def test():
#     name = edit_ism.text()
#     age = int(edit_yosh.text())

#     lbl_natija.setText(f"{name}, {2026-age}-yilda tug'ilgan")
#     lbl_natija.adjustSize()

# btn_ok = QPushButton("OK", win)
# btn_ok.setStyleSheet("font-size:50px")
# btn_ok.clicked.connect(test)
# btn_ok.move(300, 180)

#------------------------------------

# def test1():
#     print("Javohir")

# def test2():
#     print("Saliyev")

# def test3():
#     print("19")


# btn_ism=QPushButton("ism",win)
# btn_ism.setStyleSheet("font-size:50px")
# btn_ism.clicked.connect(test1)
# btn_ism.move(100,100)

# btn_fam=QPushButton("familiya",win)
# btn_fam.setStyleSheet("font-size:50px")
# btn_fam.clicked.connect(test2)
# btn_fam.move(100,250)


# btn_age=QPushButton("yosh",win)
# btn_age.setStyleSheet("font-size:50px")
# btn_age.clicked.connect(test3)
# btn_age.move(100,400)

#=====================================================



# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.v_main_lay = QVBoxLayout()

#         self.btn_red = QPushButton("RED")
#         self.btn_red.clicked.connect(self.Red)

#         self.btn_yellow = QPushButton("Yellow")
#         self.btn_yellow.clicked.connect(self.Yellow)

#         self.btn_green = QPushButton("Green")
#         self.btn_green.clicked.connect(self.Green)

#         self.v_main_lay.addWidget(self.btn_red)
#         self.v_main_lay.addWidget(self.btn_yellow)
#         self.v_main_lay.addWidget(self.btn_green)

#         self.setLayout(self.v_main_lay)

#     def Red(self):
#         self.setStyleSheet("background:red")
#         self.btn_green.setStyleSheet("background: white")
#         self.btn_red.setStyleSheet("background: white")
#         self.btn_yellow.setStyleSheet("background: white")

#     def Yellow(self):
#         self.setStyleSheet("background:yellow")
#         self.btn_green.setStyleSheet("background: white")
#         self.btn_red.setStyleSheet("background: white")
#         self.btn_yellow.setStyleSheet("background: white")
        
#     def Green(self):
#         self.setStyleSheet("background:green")
#         self.btn_green.setStyleSheet("background: white")
#         self.btn_red.setStyleSheet("background: white")
#         self.btn_yellow.setStyleSheet("background: white")


# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()

#--------------------------------------------------------------

# from random import choice

# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout

# class window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.is_on=True
#         self.count=0

#         self.v_main_lay=QVBoxLayout()
#         self.h_lbl_lay=QHBoxLayout()
#         self.h_btn_lay=QHBoxLayout()

#         self.lbl1=QLabel()
#         self.lbl1.setText("0")

#         self.lbl2=QLabel()
#         self.change()
#         self.btn_change=QPushButton("Change")
#         self.btn_change.clicked.connect(self.change)

#         self.btn_clear=QPushButton("clrear")
#         self.btn_clear.clicked.connect(self.clear)
#         self.btn_plus=QPushButton("+")
#         self.btn_plus.clicked.connect(self.plus)
#         self.btn_on=QPushButton("on/off")
#         self.btn_on.clicked.connect(self.on)

#         self.h_lbl_lay.addWidget(self.lbl2)
#         self.h_lbl_lay.addWidget(self.btn_change)

#         self.h_btn_lay.addWidget(self.btn_clear)
#         self.h_btn_lay.addWidget(self.btn_plus)
#         self.h_btn_lay.addWidget(self.btn_on)

#         self.v_main_lay.addWidget(self.lbl1)
#         self.v_main_lay.addLayout(self.h_lbl_lay)
#         self.v_main_lay.addLayout(self.h_btn_lay)

#         self.setLayout(self.v_main_lay)



#     def change(self):
#         if self.is_on:
#             zikrla=["Subhanollox","Alxamdulillax","Astag'firoullox","Ollohu akbar"]
#             self.zikr=choice(zikrla)
#             self.lbl2.setText(self.zikr)
#             self.clear()

#     def clear(self):
#         if self.is_on:
#             self.lbl1.clear()
#             self.count=0

#     def plus(self):
#         if self.is_on:
#             self.count += 1
#             self.lbl1.setText(str(self.count))

#     def on(self):
#         self.is_on=not self.is_on
#         self.btn_clear.setEnabled(self.is_on)
#         self.btn_plus.setEnabled(self.is_on)
#         self.btn_change.setEnabled(self.is_on)
        



# app = QApplication([])
# win = window()
# win.show()
# app.exec_()


#======================================

#           ===2-dars===

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,QLabel, QMessageBox, QCheckBox

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setStyleSheet("font-size:20px")

#         self.msg=QMessageBox()

#         self.v_main_lay=QVBoxLayout()
#         self.h_btn_lay=QHBoxLayout()

#         self.main_lbl=QLabel("---Menu---")
#         self.lbl_1=QLabel("1-ovqatla:")
#         self.lbl_2=QLabel("2-ovqatla:")
#         self.lbl_drink=QLabel("Ichimlila:")

#         self.bir_c1=QCheckBox("Sho'rva:67000")
#         self.bir_c2=QCheckBox("Mastava:76000")
#         self.bir_c3=QCheckBox("Moxora:70000")
#         self.bir_c4=QCheckBox("Nampar:80000")
#         self.bir_c5=QCheckBox("Lag'mon:69000")
#         self.lst1=[self.bir_c1,self.bir_c2,self.bir_c3,self.bir_c4,self.bir_c5]

#         self.ikki_c1=QCheckBox("Osh:90000")
#         self.ikki_c2=QCheckBox("Qozon kabob:120000")
#         self.ikki_c3=QCheckBox("Shashli:45000")
#         self.ikki_c4=QCheckBox("Kallapocha:340000")
#         self.ikki_c5=QCheckBox("Norin:60000")
#         self.lst2=[self.ikki_c1,self.ikki_c2,self.ikki_c3,self.ikki_c4,self.ikki_c5]

#         self.uch_c1=QCheckBox("Qora choy:30000")
#         self.uch_c2=QCheckBox("Ko'k choy:30000")
#         self.uch_c3=QCheckBox("Kola:45000")
#         self.uch_c4=QCheckBox("Pepsi:44000")
#         self.uch_c5=QCheckBox("Fanta:45000")
#         self.lst3=[self.uch_c1,self.uch_c2,self.uch_c3,self.uch_c4,self.uch_c5]

#         self.btn_next=QPushButton("Kengisi")
#         self.btn_next.clicked.connect(self.next)
#         self.btn_exit=QPushButton("Exit")
#         self.btn_exit.clicked.connect(exit)
#         self.btn_back=QPushButton("Back")
#         self.btn_back.clicked.connect(self.back)
#         self.btn_back.hide()
#         self.btn_tastiq=QPushButton("Buyurtma berish")
#         self.btn_tastiq.clicked.connect(self.tastiq)
#         self.btn_tastiq.hide()

#         self.h_btn_lay.addWidget(self.btn_next)
#         self.h_btn_lay.addWidget(self.btn_exit)
#         self.h_btn_lay.addWidget(self.btn_back)
#         self.h_btn_lay.addWidget(self.btn_tastiq)

#         self.v_main_lay.addWidget(self.main_lbl)
#         self.v_main_lay.addWidget(self.lbl_1)
#         for i in self.lst1:
#             self.v_main_lay.addWidget(i)
#         self.v_main_lay.addWidget(self.lbl_2)
#         for i in self.lst2:
#             self.v_main_lay.addWidget(i)
#         self.v_main_lay.addWidget(self.lbl_drink)
#         for i in self.lst3:
#             self.v_main_lay.addWidget(i)
#         self.v_main_lay.addLayout(self.h_btn_lay)
#         self.setLayout(self.v_main_lay)

#     def back(self):
#         self.main_lbl.setText("---Menu---")
#         self.btn_tastiq.hide()
#         self.btn_back.hide()
#         self.btn_next.show()

#         for i in self.lst1:
#             i.show()
#         for i in self.lst2:
#             i.show()
#         for i in self.lst3:
#             i.show()

#     def tastiq(self):
#         self.msg.setIcon(QMessageBox.Information)
#         self.msg.setText("Buyurtma qabul qilindi, tez orada buyurtmangiz olib kelinadi!")
#         self.msg.setWindowTitle("Xabar")
#         self.msg.exec_()

#     def next(self):
#         self.btn_next.hide()
#         self.btn_back.show()
#         self.btn_tastiq.show()

#         pul=0

#         for i in self.lst1:
#             if i.isChecked():
#                 pul+=int(i.text().split(":")[1])
#             else:
#                 i.hide()
#         for i in self.lst2:
#             if i.isChecked():
#                 pul+=int(i.text().split(":")[1])
#             else:
#                 i.hide()
#         for i in self.lst3:
#             if i.isChecked():
#                 pul+=int(i.text().split(":")[1])
#             else:
#                 i.hide()

#         self.lbl_1.hide()
#         self.lbl_2.hide()
#         self.lbl_drink.hide()

#         self.main_lbl.setText(f"Jami narx: {pul}")

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()



#  ======================================

#           ===3-dars===

# from PyQt5.QtWidgets import * 

# class SecondWindow(QWidget):
#     def __init__(self, obj):
#         super().__init__()

#         self.b_btn_lay = QVBoxLayout()

#         self.lbl_name=QLabel(f"Name: {obj.ism}")
#         self.lbl_second=QLabel(f"Second: {obj.fam}")
#         self.lbl_age=QLabel(f"Age: {obj.yosh}")

#         self.btn_back = QPushButton("Exit")
#         self.btn_back.clicked.connect(exit)

#         self.b_btn_lay.addWidget(self.lbl_name)
#         self.b_btn_lay.addWidget(self.lbl_second)
#         self.b_btn_lay.addWidget(self.lbl_age)
#         self.b_btn_lay.addWidget(self.btn_back)
#         self.setLayout(self.b_btn_lay)

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.v_main_lay = QVBoxLayout()

#         self.name=QLineEdit()
#         self.name.setPlaceholderText("Name...")

#         self.second=QLineEdit()
#         self.second.setPlaceholderText("Second...")

#         self.age=QLineEdit()
#         self.age.setPlaceholderText("Age...")

#         self.btn_next = QPushButton("NEXT")
#         self.btn_next.clicked.connect(self.Next)

#         self.v_main_lay.addWidget(self.name)
#         self.v_main_lay.addWidget(self.second)
#         self.v_main_lay.addWidget(self.age)
#         self.v_main_lay.addWidget(self.btn_next)

#         self.setLayout(self.v_main_lay)

#     def Next(self):
#         self.close()
#         self.ism=self.name.text()
#         self.fam=self.second.text()
#         self.yosh=self.age.text()
#         self.window_second = SecondWindow(self)
#         self.window_second.show()

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()

#------------------------------------------------------------

# from PyQt5.QtWidgets import * 

# class ThirdWindow(QWidget):
#     def __init__(self, obj, shahar):
#         super().__init__()

#         self.window_second = obj

#         self.tumanla = {
#         "Toshken": ["Chilonzor", "Yunusobod", "Mirzo Ulug'bek"],
#         "Samarqan": ["Samarqand shahar", "Bulung'ur", "Jomboy"],
#         "Andijon": ["Andijon shahar", "Asaka", "Xo'jaobod"],
#         "California": ["Los Angeles", "San Francisco", "San Diego"],
#         "Texas": ["Houston", "Dallas", "Austin"],
#         "Georgia": ["Atlanta", "Savannah", "Augusta"],
#         "London": ["Westminster", "Camden", "Greenwich"],
#         "Manchester": ["City Centre", "Salford", "Trafford"],
#         "Liverpool": ["City Centre", "Wavertree", "Anfield"],
#         }

#         self.v_main_lay = QVBoxLayout()
#         self.h_btn_lay=QHBoxLayout()

#         self.btn_back = QPushButton("Back")
#         self.btn_back.clicked.connect(self.Back)
#         self.btn_ex = QPushButton("Exit")
#         self.btn_ex.clicked.connect(exit)

#         self.h_btn_lay.addWidget(self.btn_back)
#         self.h_btn_lay.addWidget(self.btn_ex)

#         for i in self.tumanla.get(shahar,[]):
#             self.v_main_lay.addWidget(QLabel(i))
#         self.v_main_lay.addLayout(self.h_btn_lay)
#         self.setLayout(self.v_main_lay)

#     def Back(self):
#         self.close()
#         self.window_second.show()

# class SecondWindow(QWidget):
#     def __init__(self, obj):
#         super().__init__()

#         self.window_main = obj

#         self.v_main_lay=QVBoxLayout()
#         self.h_btn_lay = QHBoxLayout()

#         self.lbl_shahar=QLabel("---Shaharla---")

#         if obj.dav=="UZB":
#             self.rd_tosh=QRadioButton("Toshken")
#             self.rd_sam=QRadioButton("Samarqan")
#             self.rd_and=QRadioButton("Andijon")
#             self.radios = [self.rd_tosh, self.rd_sam, self.rd_and]
#         elif obj.dav=="USA":
#             self.rd_ca=QRadioButton("California")
#             self.rd_te=QRadioButton("Texas")
#             self.rd_ge=QRadioButton("Georgia")
#             self.radios = [self.rd_ca, self.rd_te, self.rd_ge]
#         else:
#             self.rd_lo=QRadioButton("London")
#             self.rd_ma=QRadioButton("Manchester")
#             self.rd_li=QRadioButton("Liverpool")
#             self.radios = [self.rd_lo, self.rd_ma, self.rd_li]
#         self.radios[0].setChecked(True)

#         self.btn_back = QPushButton("Back")
#         self.btn_back.clicked.connect(self.Back)

#         self.btn_next = QPushButton("Next")
#         self.btn_next.clicked.connect(self.Next)

#         self.h_btn_lay.addWidget(self.btn_back)
#         self.h_btn_lay.addWidget(self.btn_next)

#         self.v_main_lay.addWidget(self.lbl_shahar)
#         for rd in self.radios:
#             self.v_main_lay.addWidget(rd)
#         self.v_main_lay.addLayout(self.h_btn_lay)
#         self.setLayout(self.v_main_lay)

#     def Back(self):
#         self.close()
#         self.window_main.show()

#     def Next(self):
#         self.close()
#         for i in self.radios:
#             if i.isChecked():
#                 shahar=i.text()
#         self.window_third = ThirdWindow(self,shahar)
#         self.window_third.show()

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.v_main_lay = QVBoxLayout()

#         self.btn_next = QPushButton("NEXT")
#         self.btn_next.clicked.connect(self.Next)
#         self.lbl_davlat=QLabel("---Davlatla---")

#         self.rd_uz=QRadioButton("UZB")
#         self.rd_uz.setChecked(True)
#         self.rd_us=QRadioButton("USA")
#         self.rd_uk=QRadioButton("UK")

#         self.v_main_lay.addWidget(self.lbl_davlat)
#         self.v_main_lay.addWidget(self.rd_uz)
#         self.v_main_lay.addWidget(self.rd_us)
#         self.v_main_lay.addWidget(self.rd_uk)
#         self.v_main_lay.addWidget(self.btn_next)
#         self.setLayout(self.v_main_lay)

#     def Next(self):
#         self.close()
#         if self.rd_uz.isChecked():
#             self.dav=self.rd_uz.text()
#         elif self.rd_us.isChecked():
#             self.dav=self.rd_us.text()
#         else:
#             self.dav=self.rd_uk.text()

#         self.window_second = SecondWindow(self)
#         self.window_second.show()

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()


#-----------------------------------------------------------------
# from PyQt5.QtWidgets import *
# import json

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.v_main_lay=QVBoxLayout()
#         self.h_jins_lay=QHBoxLayout()

#         self.lbl=QLabel("🧑‍💻 Empolyee Management")

#         self.edit_search=QLineEdit()
#         self.edit_search.setPlaceholderText("Enter employee fullname")
#         self.btn_search=QPushButton("🔎 Search Employee")
#         self.btn_search.clicked.connect(self.search)
#         self.lbl_fullname=QLabel("Full Name")
#         self.age=QLabel("Age")
#         self.number=QLabel("Phone number")
#         self.email=QLabel("Email")
#         self.rd_male=QRadioButton("Male")
#         self.rd_female=QRadioButton("Female")
#         self.cm=QComboBox()
#         self.cm.addItems(["Backend","Frontend","Cybersecuraty","AI",])
#         self.btn_edit=QPushButton("Edit employee")
#         self.btn_edit.clicked.connect(self.edit)

#         self.h_jins_lay.addWidget(self.rd_male)
#         self.h_jins_lay.addWidget(self.rd_female)

#         self.v_main_lay.addWidget(self.lbl)
#         self.v_main_lay.addWidget(self.edit_search)
#         self.v_main_lay.addWidget(self.btn_search)
#         self.v_main_lay.addWidget(self.lbl_fullname)
#         self.v_main_lay.addWidget(self.age)
#         self.v_main_lay.addWidget(self.number)
#         self.v_main_lay.addWidget(self.email)
#         self.v_main_lay.addLayout(self.h_jins_lay)
#         self.v_main_lay.addWidget(self.cm)
#         self.v_main_lay.addWidget(self.btn_edit)
#         self.setLayout(self.v_main_lay)

#     def search(self):
#         oti=self.edit_search.text()
#         with open("employee.json") as f:
#             data=json.load(f)
#             a=data.keys()
#             if oti in data:
#                 self.lbl_fullname.setText(data[oti])
#             else:
#                 QMessageBox.warning(self,"error","Bunaqa ismli ishchi topilmadi")
            

#     def edit(self):
#         pass 

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()