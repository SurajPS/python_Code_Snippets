# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 12:24:59 2018

@author: Z637257
"""

import csv
import math



def get_data(csvname):
  d=csv.reader(open(csvname,'r'))
  latlon=[]
  firstrow=True
  for row in d:
    if firstrow:
      firstrow=False
      continue
    vals=[row[1],row[2]]
    latlon=latlon+[vals]
  latlon.pop(0)
  return latlon

  

def get_kml(csvname, targetkml):
  vals=get_data(csvname)

  kmldata_boundary = open(targetkml,'w')  
  kmldata_boundary.write("<?xml version='1.0' encoding='UTF-8'?>\n")
  kmldata_boundary.write("<kml xmlns='http://www.opengis.net/kml/2.2' xmlns:gx='http://www.google.com/kml/ext/2.2'>\n")
  kmldata_boundary.write("<Document>\n")
  kmldata_boundary.write("   <name>Trajectory: Path </name>\n")

  kmldata_boundary.write('''
  <Style id="yellowLineGreenPoly">
      <LineStyle>
        <color>7f0000ff</color>
        <width>4</width>
      </LineStyle>
      <PolyStyle>
        <color>7f00ff00</color>
      </PolyStyle>
    </Style>
    <Placemark>
      <name>Absolute Extruded</name>
      <description>Transparent green wall with yellow outlines</description>
      <styleUrl>#yellowLineGreenPoly</styleUrl>
      <LineString>
        <extrude>1</extrude>
        <tessellate>1</tessellate>
        <altitudeMode>absolute</altitudeMode>
        <coordinates> ''')

  for latlong in vals:
    kmldata_boundary.write(str(latlong[1])+","+str(latlong[0])+"\n")


  kmldata_boundary.write('''        </coordinates>
      </LineString>
    </Placemark>
  </Document>
  </kml>
  ''')
  kmldata_boundary.close()
  


#get_kml('input.csv','output.kml')
