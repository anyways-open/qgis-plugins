# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ToolBoxDialog
                                 A QGIS plugin
 This plugin is a suite of tools for the ImPact Analysis
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-27
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Hamed Eftekhar @ ANYWAYS
        email                : hamed@anyways.eu
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
from qgis.PyQt.QtWidgets import QDialog, QFileDialog
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsProject
from .ImPact_toolbox_dialog_base import Ui_APIRequestDialogBase

class ToolBoxDialog(QDialog, Ui_APIRequestDialogBase):

    def __init__(self, parent=None):
        """Constructor."""
        super(ToolBoxDialog, self).__init__(parent)

        #load UI
        self.setupUi(self)
        
        key_path=os.path.dirname(os.path.realpath(__file__))+"/RoutingAPI_Key.txt"
        try:
            ExistingKey=open(key_path, "r+").read()
            self.routingTab_KeyHolder.setText(ExistingKey)
        except IOError:
            self.routingTab_KeyHolder.setText("")
            
        dir_path = QgsProject.instance().readPath("./")
        if dir_path == "./" :
            self.routingTab1_outDirTxt.setText("")
            self.routingTab2_outDirTxt.setText("")
        else:
            self.routingTab1_outDirTxt.setText(dir_path)
            self.routingTab2_outDirTxt.setText(dir_path)
            
        #connect eventhandlers
        self.routingTab1_OutDirBtn.clicked.connect( self.dir1clicked )
        self.routingTab2_OutDirBtn.clicked.connect( self.dir2clicked )


    #eventhandlers 
    dir1clicked = lambda self: self.routingTab1_outDirTxt.setText(
         QFileDialog.getExistingDirectory(self, "Select a directory to save routings", "") )
    dir2clicked = lambda self: self.routingTab2_outDirTxt.setText(
         QFileDialog.getExistingDirectory(self, "Select a directory to save routings", "") )
