import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget, QLineEdit, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector
 #
 # Created by DMSoftware-comminuty.
 # autor: D.M. Holiness
 # User: user
 # Date: 23/05/2022
 # Time: 09:47
 # To change this template use Tools | Options | Coding | Edit Standard Headers.

code_client = 0
class StartApp(QDialog):
    def __init__(self):
        super(StartApp, self).__init__()
        loadUi("views/start.ui", self)
        self.s_b1.clicked.connect(self.reg)
        self.pushButton_2.clicked.connect(self.log)

    def reg(self):
        widget.setCurrentIndex(2)
    def log(self):
        widget.setCurrentIndex(1)

class LoginApp(QDialog):
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi("views/Login-form.ui", self)
        self.b1.clicked.connect(self.login)

        self.LineEditUsrn = QtWidgets.QLineEdit(widget)
        self.LineEditUsrn.setObjectName("tb1_")

        self.LineEditPwd = QtWidgets.QLineEdit(widget)
        self.LineEditPwd.setObjectName("tb2")
        self.pushButton.clicked.connect(self.linkRegist)

    def linkRegist(self):
            widget.setCurrentIndex(2)

    def login(self):
        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        usern = self.tb1_.text()
        code = self.tb2.text()
        myCursor = dbcon.cursor()
        myCursor.execute("SELECT * FROM client WHERE code = '"+code+"'")
        result = myCursor.fetchone()

        if result:
           widget.setCurrentIndex(3)
        else:
           QMessageBox.information(self,"Message","Vous n'etes pas autorisé, veuillez créer un compte puis reesayez")
        

class EspaceClient(QDialog):
    def __init__(self):
        super(EspaceClient, self).__init__()
        loadUi("views/espace-compte.ui", self)
        self.b1.clicked.connect(self.logout)
        self.vers1.clicked.connect(self.verse)
        self.ret1.clicked.connect(self.retrait)
        self.virm.clicked.connect(self.virem)
        self.Annuler.clicked.connect(self.annul)
        self.b9.clicked.connect(self.menu)
        self.pushButton.clicked.connect(self.show)
        self.pushButton_2.clicked.connect(self.show_2)

        self.LineEditMontant1 = QtWidgets.QLineEdit(widget)
        self.LineEditMontant1.setObjectName("lineEditMontant1")

        self.LineEditMontant2 = QtWidgets.QLineEdit(widget)
        self.LineEditMontant2.setObjectName("lineEditMontant2")

        self.LineEditCode = QtWidgets.QLineEdit(widget)
        self.LineEditCode.setObjectName("lineEditCode")

        self.LineEditCode_2 = QtWidgets.QLineEdit(widget)
        self.LineEditCode_2.setObjectName("lineEditCode_2")

        self.LineEditMontant3 = QtWidgets.QLineEdit(widget)
        self.LineEditMontant3.setObjectName("lineEditMontant3")

        self.LineEditCompte_3 = QtWidgets.QLineEdit(widget)
        self.LineEditCompte_3.setObjectName("lineEditCompte_3")

    def show(self):
        code = self.lineEditCode.text()

        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        myCursor = dbcon.cursor()

        myCursor.execute("SELECT * FROM client WHERE code = '"+code+"'")
        result_user = myCursor.fetchall()

        if result_user:

            code_client = result_user[0][1]
            nom_cl = result_user[0][2]
            post_cl = result_user[0][3]
            adresse = result_user[0][4]
            telephone = result_user[0][5]

            self.label_5.setText(code_client)
            self.label_6.setText(nom_cl)
            self.label_8.setText(post_cl)
            self.label_12.setText(adresse)
            self.label_10.setText(telephone)

    def show_2(self):
        code = self.lineEditCode_2.text()

        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        myCursor = dbcon.cursor()
        myCursor.execute("SELECT * FROM compte WHERE code = '"+code+"'")
        result = myCursor.fetchall()

        if result:
            #
            code_cpt = result[0][1]
            solde = str(result[0][2])
            date_cpt = result[0][3]
            titulaire = str(result[0][4])

            self.code.setText(code_cpt)
            self.solde.setText(solde)
            self.type.setText(titulaire)
            self.date.setText(date_cpt)

    def logout(self):
        widget.setCurrentIndex(0)

    def verse(self):
        code = self.lineEditCode_2.text()
        montant_verse = self.lineEditMontant1.text()
        mt_verse = float(montant_verse)
       
        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        myCursor = dbcon.cursor()
        myCursor.execute("SELECT * FROM compte WHERE code = '"+code+"'")
        result = myCursor.fetchall()

        if result:

            solde = result[0][2]

            nx_sold = mt_verse + solde
            myCursor.execute("UPDATE compte SET solde = '"+str(nx_sold)+"'")
            dbcon.commit()
            QMessageBox.information(self,"Message","Votre compte a été alimenté, votre nouveau solde est '"+str(nx_sold)+"'")
            self.lineEditMontant1.setText("")
        else:
           QMessageBox.information(self,"Message","compte non reconnu")

    def retrait(self):
        code = self.lineEditCode_2.text()
        montant_verse = self.lineEditMontant2.text()
        mt_verse = float(montant_verse)

        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        myCursor = dbcon.cursor()
        myCursor.execute("SELECT * FROM compte WHERE code = '"+code+"'")
        result = myCursor.fetchall()

        if result:

            solde = result[0][2]

            nx_sold = solde - mt_verse
            myCursor.execute("UPDATE compte SET solde = '"+str(nx_sold)+"'")
            dbcon.commit()
            QMessageBox.information(self,"Message","Votre compte a été credité, votre nouveau solde est '"+str(nx_sold)+"'")
            self.lineEditMontant2.setText("")
        else:
           QMessageBox.information(self,"Message","compte non reconnu")

    def virem(self):
        code = self.lineEditCode_2.text()
        montant_vire = self.lineEditMontant3.text()
        compte_e = self.lineEditCompte_3.text()

        mt_vire = float(montant_vire)

        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        myCursor = dbcon.cursor()
        myCursor.execute("SELECT * FROM compte WHERE code = '"+code+"'")
        result = myCursor.fetchall()

        if result:

            solde = result[0][2]
            nx_sold = solde - mt_vire

            myCursor.execute("UPDATE compte SET solde = '"+str(nx_sold)+"'")
            dbcon.commit()

            myCursor.execute("SELECT * FROM compte WHERE code = '"+compte_e+"'")
            result_cpt2 = myCursor.fetchall()
            if result_cpt2:

                solde2 = result_cpt2[0][2]
                nx_sold2 = solde2 + mt_vire

                myCursor.execute("UPDATE compte SET solde = '"+str(nx_sold2)+"'")
                dbcon.commit()
                QMessageBox.information(self,"Message","Votre virement a reussi, votre nouveau solde est '"+str(nx_sold)+"'")
                self.lineEditMontant3.setText("")
            else:
                QMessageBox.information(self,"Message","compte destinateur non reconnu")
        else:
           QMessageBox.information(self,"Message","compte non reconnu")

    def annul(self):
        widget.setCurrentIndex(3)

    def menu(self):
        widget.setCurrentIndex(4)

class InsertApp(QDialog):
    def __init__(self):
        super(InsertApp, self).__init__()
        loadUi("views/Insert-form.ui", self)


        self.Affiche.clicked.connect(self.afficher)
        self.Annuler.clicked.connect(self.annul)
        self.Creer.clicked.connect(self.creat)
        self.Menu.clicked.connect(self.menu)

        self.LineEditCode = QtWidgets.QLineEdit(widget)
        self.LineEditCode.setObjectName("lineEditCode")

        self.LineEditSolde = QtWidgets.QLineEdit(widget)
        self.LineEditSolde.setObjectName("lineEditSolde")

        self.DateTimeEdit = QtWidgets.QDateTimeEdit(widget)
        self.DateTimeEdit.setObjectName("dateTimeEdit")

        self.LineEditCode_2 = QtWidgets.QLineEdit(widget)
        self.LineEditCode_2.setObjectName("lineEditCode_2")

        self.LineEditCode_3 = QtWidgets.QLineEdit(widget)
        self.LineEditCode_3.setObjectName("lineEditCode_3")


    def afficher(self):
        code = self.lineEditCode_3.text()
        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        myCursor = dbcon.cursor()
        myCursor.execute("SELECT * FROM client WHERE code = '"+code+"'")
        result = myCursor.fetchall()

        if result:
            code_client = result[0][1]
            nom_cl = result[0][2]
            post_cl = result[0][3]
            adresse = result[0][4]
            telephone = result[0][5]

            self.label_6.setText(nom_cl)
            self.label_8.setText(post_cl)
            self.label_12.setText(adresse)
            self.label_10.setText(telephone)
        else:
            # COMMENT
            QMessageBox.information(self,"Message","Veuillez vous deconnecter pour effectuer cette action")
    def annul(self):

        self.lineEditCode.setText("")
        self.lineEditCode_2.setText("")
        self.lineEditSolde.setText("")

    def creat(self):
        code_cpt = self.lineEditCode.text()
        code_cl = self.lineEditCode_2.text()
        date_cpt = self.dateTimeEdit.text()
        solde = self.lineEditSolde.text()

        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        Cursor = dbcon.cursor()
        Cursor.execute("SELECT * FROM compte WHERE code = '"+code_cpt+"'")
        result = Cursor.fetchone()
        # nomber = myCursor.rowcount

        Cursor.execute("SELECT * FROM client WHERE code = '"+code_cl+"'")
        result_user = Cursor.fetchone()

        if result_user:
            if result:
                QMessageBox.information(self,"Message","Ce compte existe deja!!")
            else:
                Cursor.execute("INSERT INTO compte VALUE(NULL,'"+code_cpt+"','"+solde+"','"+date_cpt+"','"+code_cl+"')")
                dbcon.commit()
                QMessageBox.information(self,"Message","nouveau compte créé")
        else:
            QMessageBox.information(self,"Message","utilisateur non identifié!!")

    def menu(self):
        widget.setCurrentIndex(3)

class Registerform(QDialog):
    def __init__(self):
        super(Registerform,self).__init__()
        loadUi("views/Register-form.ui", self)
        self.b3.clicked.connect(self.log)

        self.LineEditCode = QtWidgets.QLineEdit(widget)
        self.LineEditCode.setObjectName("tb3_2")

        self.LineEditNom = QtWidgets.QLineEdit(widget)
        self.LineEditNom.setObjectName("tb3")

        self.LineEditPostNom = QtWidgets.QDateTimeEdit(widget)
        self.LineEditPostNom.setObjectName("tb4")

        self.LineEditAdresse = QtWidgets.QLineEdit(widget)
        self.LineEditAdresse.setObjectName("tb5")

        self.LineEditTel = QtWidgets.QLineEdit(widget)
        self.LineEditTel.setObjectName("tb6")

    def log(self):
        code = self.tb3_2.text()
        nom = self.tb3.text()
        postnom = self.tb4.text()
        adresse = self.tb5.text()
        tel = self.tb6.text()

        dbcon = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "",
            db = "db_compte"
        )
        Cursor = dbcon.cursor()

        Cursor.execute("SELECT * FROM client WHERE code = '"+code+"'")
        result_user = Cursor.fetchone()

        if result_user:
            QMessageBox.information(self,"Message","client déja existant!!")
        else:
            Cursor.execute("INSERT INTO client VALUE(NULL,'"+code+"','"+nom+"','"+postnom+"','"+adresse+"','"+tel+"')")
            dbcon.commit()
            QMessageBox.information(self,"Message","Opreationeffectuée avec succés!!")
            widget.setCurrentIndex(1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
StartForm = StartApp()
Insertform = InsertApp()
LoginForm = LoginApp()
EspaceClient = EspaceClient()
Registerform = Registerform()

widget.addWidget(StartForm) #0
widget.addWidget(LoginForm) #1
widget.addWidget(Registerform)#2
widget.addWidget(EspaceClient) #3
widget.addWidget(Insertform)#4


w = 881
h = 551

widget.setCurrentIndex(0)
widget.setFixedWidth(871)
widget.setFixedHeight(552)
widget.show()

app.exec_()
