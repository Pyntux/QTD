import gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDate
import datetime
import sys
import os

# sys.path.append('/usr/share/qtd/')


# TODO:

# Srediti obaveštenja u label.info:
#   kad je "minutes" a kad "minute", "hour" i "hours"
#   ili namestiti da obaveštenje kaže tačno vreme kad će akcija da se desi

# Srediti i obaveštenja kad se prlazi sa opcije na opciju combo boxova

# Srediti tray obaveštenja

class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        """######################
        ## Namešta spinBox-ove ##
        ## i njihove vrednosti ##
        ######################"""
        self.time_set()

        """#######################
        ##  Neophodno za timer  ##
        ##  za delay akcija     ##
        #######################"""
        self.timer = None

        """############################
        ##  Ubacivanje TRAY-a u gui  ##
        ############################"""
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setToolTip("QTD")
        self.icon = QIcon("icons/shutdown.ico")
        self.tray.setIcon(self.icon)
        self.tray.setVisible(False)  # Tray nije vidljiv dok se ne klikne dugme "tray_button"

        # menu
        self.menu = QtWidgets.QMenu()
        self.tray.setContextMenu(self.menu)

        self.option1_icon = QIcon("icons/show.ico")
        self.option1 = QtWidgets.QAction("Show QTD")
        self.option1.setIcon(self.option1_icon)
        self.option1.triggered.connect(self.show_from_tray)
        self.menu.addAction(self.option1)

        self.option2_icon = QIcon("icons/reset.ico")
        self.option2 = QtWidgets.QAction("Reset schedule")
        self.option2.setIcon(self.option2_icon)
        self.option2.triggered.connect(self.reset)
        self.menu.addAction(self.option2)

        self.option3_icon = QIcon("icons/exit.ico")
        self.option3 = QtWidgets.QAction("Exit application")
        self.option3.setIcon(self.option3_icon)
        self.option3.triggered.connect(self.exit)
        self.menu.addAction(self.option3)
        ## /END ####################################################################

        """#####################
        ##  Timer za LCD sat  ##
        #####################"""
        self.timer_lcd = QtCore.QTimer()
        self.timer_lcd.timeout.connect(self.showTime)
        self.timer_lcd.start()
        ## /END ####################################################################

        """#############################################
        ##  Pozivanje funkcija koje reaguju na        ##
        ##  promenu stanja comboBox-ova i sakrivanje  ##
        ##  spinBox-ova(HH:MM) i labela za početno    ##
        ##  stanje programa                           ##
        #############################################"""
        self.comboBox_action.activated[str].connect(self.combo_1)
        self.comboBox_make_in.activated[str].connect(self.combo_2)
        self.spinBox_hour.hide()
        self.spinBox_min.hide()
        self.label_icon.hide()
        ## /END ####################################################################

        """###############################################
        ##  Povezivanje dugmića sa njihovim funkcijama  ##
        ################################################"""
        self.apply_button.clicked.connect(self.apply)
        self.reset_button.clicked.connect(self.reset)
        self.tray_button.clicked.connect(self.minimize)
        self.exit_button.clicked.connect(self.exit)
        ## /END ####################################################################

#-----------------------#
# FUNKCIJE APLIKACIJE:  #
#-----------------------#

    """###########################################
    ## Funkcije za promenu stanja comboBox-ova: ##
    ###########################################"""

    """ Kako se promeni opcija prvog comboBox-a
    daje obaveštenje o tome šta odabrana akcija radi"""

    def combo_1(self, text):
        item = text
        if item == "Shutdown":
            self.label_info.setText(
                "This option will turn off your PC ...")
        elif item == "Reboot":
            self.label_info.setText("This option will restart your PC ...")
        elif item == "Hibernate":
            self.label_info.setText("This option will hibernate your PC ...")
        elif item == "Sleep":
            self.label_info.setText("This option will put your PC to sleep ...")
    ## /END ####################################################################

    """ Kako se promeni opcija drugog comboBox-a
    prikazuje ili krije spinBox-ove i label zavisno od odabrane opcije
    i daje obaveštenje da treba odabrati minute, sate ili tačno vreme"""

    def combo_2(self, text):
        item = text
        if item == "Minutes from now":
            self.spinBox_single.show()
            self.spinBox_hour.hide()
            self.spinBox_min.hide()
            self.label_icon.hide()
            self.label_info.setText(
                f"In how many minutes to perform {self.comboBox_action.currentText()}?")
        elif item == "Hours from now":
            self.spinBox_single.show()
            self.spinBox_hour.hide()
            self.spinBox_min.hide()
            self.label_icon.hide()
            self.label_info.setText(
                f"In how many hours to perform {self.comboBox_action.currentText()}?")
        elif item == "At selected time":
            self.spinBox_single.hide()
            self.spinBox_hour.show()
            self.spinBox_min.show()
            self.label_icon.hide()
            self.label_info.setText(
                f"Choose time (HH:MM) to schedule {self.comboBox_action.currentText()}!")
        elif item == "Now":
            self.spinBox_single.hide()
            self.spinBox_hour.hide()
            self.spinBox_min.hide()
            self.label_icon.show()
            self.label_info.setText(
                f"{self.comboBox_action.currentText()} will be executed without delay!")
        ## /END ####################################################################

    """####################################################
    ## Velika APPLY funkcija koja odrađuje najveći posao ##
    ##           vezana je za "apply_button"             ##
    ####################################################"""

    def apply(self):
        """ Neophodne vrednosti """
        item = self.comboBox_action.currentText()
        item_2 = self.comboBox_make_in.currentText()
        value_hm = self.spinBox_single.value()
        value_hour = self.spinBox_hour.value()
        value_min = self.spinBox_min.value()

        """KOMENTAR:
        - SHUTDOWN ne koristi funkcije jer samim programom može da se svaka radnja odloži...
        - Sve ostale opcije, REBOOT, HIBERNATE i SLEEP, koriste timer za odlaganje i pozivaju funkcije
        """

        ###############
        ## SHUTDOWN: ##
        ###############

        if item == "Shutdown":
            if item_2 == "Minutes from now":
                os.system(f"shutdown -h {value_hm}")
                self.label_info.setText(f"Your PC will shutdown in {value_hm} minutes !")
            elif item_2 == "Hours from now":
                value_in_hours = value_hm * 60
                os.system(f"shutdown -h {value_in_hours}")
                self.label_info.setText(f"Your PC will shutdown in {value_hm} hours !")
            elif item_2 == "At selected time":
                os.system(f"shutdown {value_hour}:{value_min}")
                self.label_info.setText(f"Your PC will shutdown at {value_hour}:{value_min} !")
            elif item_2 == "Now":
                os.system("shutdown -h now")

        #############
        ## REBOOT: ##
        #############
        elif item == "Reboot":
            if item_2 == "Minutes from now":
                self.in_minutes(self.reboot)
            elif item_2 == "Hours from now":
                self.in_hours(self.reboot)
            elif item_2 == "At selected time":
                self.at_selected_time(self.reboot)
            elif item_2 == "Now":
                os.system("reboot")

        ################
        ## HIBERNATE: ##
        ################

        elif item == "Hibernate":
            if item_2 == "Minutes from now":
                self.in_minutes(self.hibernate)
            elif item_2 == "Hours from now":
                self.in_hours(self.hibernate)
            elif item_2 == "At selected time":
                self.at_selected_time(self.hibernate)
            elif item_2 == "Now":
                os.system("systemctl hibernate")

        ############
        ## SLEEP: ##
        ############

        elif item == "Sleep":
            if item_2 == "Minutes from now":
                self.in_minutes(self.sleep)
            elif item_2 == "Hours from now":
                self.in_hours(self.sleep)
            elif item_2 == "At selected time":
                self.at_selected_time(self.sleep)
            elif item_2 == "Now":
                os.system("systemctl suspend")

        ###############################################
        ## Disable-uje oba comboBox-a i apply_button ##
        ###############################################

        self.enable_disable_gui(False)
    ## /END ####################################################################

    """##############################
    ## Funkcije glavnih operacija: ##
    ##############################"""

    def reboot(self):
        os.system("reboot")

    def hibernate(self):
        os.system("systemctl hibernate")

    def sleep(self):
        os.system("systemctl suspend")
    ## /END ####################################################################

    """##################################################
    ## Funkcije za blokiranje delova gui-a po potrebi: ##
    ## koristi je apply funkcija i reset funkcija      ##
    ## samo se ubaci drugi "bool" parametar            ##
    ##################################################"""
    # SA JEDNOM FUNKCIJOM:

    def enable_disable_gui(self, bool):
        self.apply_button.setEnabled(bool)
        self.comboBox_action.setEnabled(bool)
        self.comboBox_make_in.setEnabled(bool)

    ## /END ####################################################################

    """##############################################################################
    ## Funkcije izvršenja akcija "za X minuta", "za X sati" ili "u određeno vreme" ##
    ## Svaka funkcija se koristi za sve akcije - Reboot, Hibernate i Sleep,        ##
    ## samo se funkciji prosledi kao drugi argument "func", tj. radnja (funkcija)  ##
    ## koju da poziva: self.reboot(); self.hibernate() ili self.sleep()            ##
    ## !vidi apply funkciju iznad!                                                 ##
    ##############################################################################"""

    def in_minutes(self, func):
        value = self.spinBox_single.value()
        value_ms = value * 60000
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.setSingleShot(True)
        self.timer.start(value_ms)
        item = self.comboBox_action.currentText()
        self.label_info.setText(f"Your PC will {str.lower(item)} in {value} minutes !")
    ## /END ####################################################################

    def in_hours(self, func):
        value = self.spinBox_single.value()
        value_ms = value * 3600000
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.setSingleShot(True)
        self.timer.start(value_ms)
        item = self.comboBox_action.currentText()
        self.label_info.setText(f"Your PC will {str.lower(item)} in {value} hours !")
    ## /END ####################################################################

    def at_selected_time(self, func):
        now = datetime.datetime.now()
        # Da odradi akciju tačno u izabrano vreme, dodao sam i sekunde u milisekunde
        now_time_in_ms = (now.second * 1000) + ((now.hour * 60 + now.minute) * 60000)
        selected_hours_in_ms = self.spinBox_hour.value() * 3600000
        selected_min_in_ms = self.spinBox_min.value() * 60000
        selected_time_in_ms = selected_hours_in_ms + selected_min_in_ms
        final_num = selected_time_in_ms - now_time_in_ms
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.setSingleShot(True)
        self.timer.start(final_num)
        item = self.comboBox_action.currentText()
        self.label_info.setText(
            f"Your PC will {str.lower(item)} at {self.spinBox_hour.value()}:{self.spinBox_min.value()} !")
    ## /END ####################################################################

    """####################################
    ## Opšte funkcije za rad aplikacije: ##
    ####################################"""

    """ Ova funkcija je pozvana u samom vrhu klase"""

    def time_set(self):
        time = datetime.datetime.now()
        self.spinBox_hour.setValue(time.hour)
        self.spinBox_hour.setMinimum(time.hour)
        self.spinBox_min.setValue(time.minute)
        self.spinBox_single.setValue(15)
    ## /END ####################################################################

    """ Ova funkcija služi za prikaz LCD sata, pozvana je iz klase"""

    def showTime(self):
        time = QTime.currentTime()
        time_text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            time_text = time.toString('hh:mm ss')
        self.lcd_clock.display(time_text)
    ## /END ####################################################################

    """####################
    ## Funkcije dugmića: ##
    ####################"""

    """ Funkcija za reset_button """

    def reset(self):
        self.timer_stop()
        self.time_set()
        self.enable_disable_gui(True)
        self.label_info.setText("Set up again!")
        #self.tray.setToolTip("TimerDown - there is no schedule!")
    ## /END ####################################################################

    """ Funkcija za stopiranje timer-a i prekid akcija shutdown programa,
    ovu funkciju poziva reset() funkcija """

    def timer_stop(self):
        if self.timer:
            self.timer.stop()
        os.system("shutdown -c")
    ## /END ####################################################################

    """ Funkcija za tray_button, minimizuje program u tray """

    def minimize(self):
        form.hide()
        self.tray.setVisible(True)
    ## /END ####################################################################

    """ Funkcija za prikaz aplikacije iz tray-a """

    def show_from_tray(self):
        form.show()
    ## /END ####################################################################

    """ Funkcija za izlazak iz aplikacije """

    def exit(self):
        sys.exit()
    ## /END ####################################################################


# KRAJ APLIKACIJE ##############################################################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle("Fusion")
    form = App()
    form.show()
    app.exec_()
