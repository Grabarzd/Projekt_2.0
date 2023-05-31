# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Projekt2
                                 A QGIS plugin
 01000110 01100001 01101010 01101110 01111001 00100000 01110100 01100101 01101110 00100000 01110000 01110010 01101111 01101010 01100101 01101011 01110100 00100000 01110100 01100001 01101011 01101001 00100000 01101110 01101001 01100101 00100000 01111010 01100001 00100000 11000101 10000010 01100001 01110100 01110111 01111001 00101100 00100000 01101110 01101001 01100101 00100000 01111010 01100001 00100000 01110100 01110010 01110101 01100100 01101110 01111001
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-31
        copyright            : (C) 2023 by DS, MR, KP 
        email                : 1
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Projekt2 class from file Projekt2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Wtyczka_Projekt_2 import Projekt2
    return Projekt2(iface)
