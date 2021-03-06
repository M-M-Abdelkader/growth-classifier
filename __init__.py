# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GrowthClassifier
                                 A QGIS plugin
 This plugin identifies patch growth type
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-08-09
        copyright            : (C) 2020 by Mahmood Abdelkader/Ahmed Elseicy
        email                : m.m.i.abdelkader@gmail.com - ahmed.elcc@gmail.com
 ***************************************************************************/

 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Mahmood Abdelkader/Ahmed Elseicy'
__date__ = '2020-08-09'
__copyright__ = '(C) 2020 by Mahmood Abdelkader/Ahmed Elseicy'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GrowthClassifier class from file GrowthClassifier.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .growth_classifier import GrowthClassifierPlugin
    return GrowthClassifierPlugin()
