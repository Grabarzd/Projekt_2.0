# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Projekt2Dialog
                                 A QGIS plugin
 01000110 01100001 01101010 01101110 01111001 00100000 01110100 01100101 01101110 00100000 01110000 01110010 01101111 01101010 01100101 01101011 01110100 00100000 01110100 01100001 01101011 01101001 00100000 01101110 01101001 01100101 00100000 01111010 01100001 00100000 11000101 10000010 01100001 01110100 01110111 01111001 00101100 00100000 01101110 01101001 01100101 00100000 01111010 01100001 00100000 01110100 01110010 01110101 01100100 01101110 01111001
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2023 by DS, MR, KP 
        email                : 1
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface
import numpy as np
from qgis.core import QgsWkbTypes, QgsVectorLayer, QgsVectorFileWriter, QgsProject, Qgis

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Wtyczka_Projekt_2_dialog_base.ui'))


class Projekt2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Projekt2Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_calculate.clicked.connect(self.option)
        self.pushButton_clear.clicked.connect(self.clear)
        

    def clear(self):
        self.label_score.setText('')
        self.label_description_of_score.setText('')
        self.label_number_of_points.setText('')
        iface.messageBar().pushInfo('Clear','Console cleaning performed correctly')

    def option(self):
        if self.checkBox_primary.isChecked() and self.checkBox_additional.isChecked() and self.radioButton_pl1992.isChecked() and self.radioButton_height.isChecked() and self.radioButtona_ares.isChecked():
            iface.messageBar().pushSuccess( 'Succes','https://www.youtube.com/shorts/O0vbnRJpsXU' )

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("                     You found a easteregg                    ")
            msg.setInformativeText('https://www.youtube.com/shorts/O0vbnRJpsXU')
            msg.setWindowTitle("Success")
            msg.exec_()

        elif self.checkBox_primary.isChecked() and self.checkBox_additional.isChecked() :
            iface.messageBar().pushCritical( 'Error','Please choose only one option (not allowed to choose both)' )
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("                     Error                    ")
            msg.setInformativeText('Please choose only one option (not allowed to choose both)')
            msg.exec_()





        elif self.checkBox_primary.isChecked():
            self.label_description_of_score.setText('Score in')
            if self.radioButton_height.isChecked():
                # układa punkty w kolejności takiej samej jak id w tabeli atrybutów
                layer = iface.activeLayer()
                choosen = layer.selectedFeatures()
                i=1
                if len(choosen)==0 or len(choosen)==1:
                        iface.messageBar().pushMessage('Please choose more points')   
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setText("                     Error                    ")
                        msg.setInformativeText('Option requires at least two points')
                        msg.exec_()
                else:
                    while i<=(len(choosen)-1):
                        delta_h=float((choosen[i].attributes())[3])-float((choosen[0].attributes())[3])
                        iface.messageBar().pushMessage(f'Różnica wysokosci pomiędzy punktami {choosen[0].attributes()[0]} oraz {choosen[i].attributes()[0]} wynosi {delta_h:.3f}')
                        i=i+1
                    iface.messageBar().pushSuccess( 'Succes','Action performed successfully' )
                self.label_score.setText('Result is in the command line') 






            elif self.radioButton_area.isChecked():
                layer = iface.activeLayer()
                choosen = layer.selectedFeatures()
                area=0
                i=0
                while i<=(len(choosen)-1):
                    if float((choosen[i].attributes())[0])==float((choosen[0].attributes())[1]):
                        last_x=float((choosen[-1].attributes())[1])
                        area=area+(float((choosen[1].attributes())[1])-last_x)*float((choosen[0].attributes())[2])
                    elif choosen[i]==choosen[-1]:
                        first_x=float((choosen[0].attributes())[1])
                        area=area+(first_x-float((choosen[-1].attributes())[2]))*float((choosen[-1].attributes())[2])
                    else:
                        delta_x=float((choosen[i+1].attributes())[1])-float((choosen[i-1].attributes())[1])
                        area=area+delta_x*float((choosen[i].attributes())[2])
                    i=i+1
                    if area<0:
                        area=area*-1
                    self.label_description_of_score.setText('Area of the designated area is')
                if self.radioButtona_meters.isChecked():
                    self.label_score.setText(f'{(area/2):.3f} m')
                elif self.radioButtona_ares.isChecked():
                    self.label_score.setText(f'{(area/200):.2f} a')
                elif self.radioButtona_hectares.isChecked():
                    self.label_score.setText(f'{(area/20000):.4f} ha')
                else:
                    self.label_description_of_score.setText('')
                    self.label_score.setText('')
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("                     Error                    ")
                    msg.setInformativeText('You have to select units of area!!!')
                    msg.exec_()






        elif self.checkBox_additional.isChecked():
            if self.radioButton_pl1992.isChecked():
                 s=1
                #QgsProject.instance().setCrs(QgsCoordinateReferenceSystem('EPSG:2180'))
            elif self.radioButton_pl2000.isChecked():
                #QgsProject.instance().setCrs(QgsCoordinateReferenceSystem('EPSG:2180'))
                s=1

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("                     Error                    ")
            msg.setInformativeText('Please choose one of the available options (Primary or Additional)')
            msg.exec_()
        selected_features=self.mMapLayerComboBox_layers.currentLayer().selectedFeatures()
        number_of_selected_elements=len(selected_features)
        self.label_number_of_points.setText(str(number_of_selected_elements))



    #def count_selected_elements(self):
        #number_of_selected_elements=10
        #selected_features=self.mMapLayerComboBox_layers.currentLayer().selectedFeatures()
        #number_of_selected_elements=len(selected_features)
        #self.label_score.setText(str(number_of_selected_elements))
        #self.label_description_of_score.setText(str('Number of choosen elements:'))
        #iface.messageBar().pushInfo( 'Score', f'{number_of_selected_elements}' )
        #iface.messageBar().pushSuccess( 'Succes','Analiza zakończona sukcesem' )
        #iface.messageBar().pushWarning( 'Ostrzeżenie','Ta operacja może być niebezpieczna' )
        #iface.messageBar().pushCritical( 'Błąd','Wystąpił błąd' )