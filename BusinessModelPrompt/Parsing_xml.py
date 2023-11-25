import xml.etree.ElementTree as ET
import csv

def Extract_Activities(root,my_Activities):
    for child in root:
        if child.tag == "{http://www.wfmc.org/2009/XPDL2.2}WorkflowProcesses":
            for first in child:
                if first.tag == "{http://www.wfmc.org/2009/XPDL2.2}WorkflowProcess":
                    for second in first:
                        if second.tag == "{http://www.wfmc.org/2009/XPDL2.2}Activities":
                            for third in second:
                                if third.tag == "{http://www.wfmc.org/2009/XPDL2.2}Activity":
                                    Activity_Name = third.attrib.get("Name", "")
                                    Activity_Id = third.attrib.get("Id", "")
                                    for forth in third:
                                        if forth.tag == "{http://www.wfmc.org/2009/XPDL2.2}NodeGraphicsInfos":
                                            for fifth in forth:
                                                if fifth.tag =="{http://www.wfmc.org/2009/XPDL2.2}NodeGraphicsInfo":
                                                    for six in fifth:
                                                        if six.tag =="{http://www.wfmc.org/2009/XPDL2.2}Coordinates":
                                                            Arow_data = []
                                                            Arow_data.append(Activity_Name)
                                                            Arow_data.append(Activity_Id)
                                                            x = six.attrib.get("XCoordinate", "")
                                                            y = six.attrib.get("YCoordinate", "")
                                                            Arow_data.append(x)
                                                            Arow_data.append(y)
                                                            my_Activities.append(Arow_data)
    Save_to_CSV_Activities(my_Activities)
    return my_Activities


def Extract_Lanes(root,my_Lanes):
    for child in root:
        if child.tag == "{http://www.wfmc.org/2009/XPDL2.2}Pools":
            for first in child:
                if first.tag == "{http://www.wfmc.org/2009/XPDL2.2}Pool":
                    for second in first:
                        if second.tag == "{http://www.wfmc.org/2009/XPDL2.2}Lanes":
                            for third in second:
                                if third.tag == "{http://www.wfmc.org/2009/XPDL2.2}Lane":
                                    Lane_Name = third.attrib.get("Name", "")
                                    Lane_Id = third.attrib.get("Id", "")
                                    for forth in third:
                                        if forth.tag == "{http://www.wfmc.org/2009/XPDL2.2}NodeGraphicsInfos":
                                            for fifth in forth:
                                                if fifth.tag =="{http://www.wfmc.org/2009/XPDL2.2}NodeGraphicsInfo":
                                                    for six in fifth:
                                                        if six.tag =="{http://www.wfmc.org/2009/XPDL2.2}Coordinates":
                                                            Lane_X = six.attrib.get("XCoordinate", "")
                                                            Lane_Y= six.attrib.get("YCoordinate", "")
                                                            Lane_H= fifth.attrib.get("Height", "")
                                                            data_rowl = []
                                                            data_rowl.append(Lane_Name)
                                                            data_rowl.append(Lane_Id)
                                                            data_rowl.append(Lane_X)
                                                            data_rowl.append(Lane_Y)
                                                            data_rowl.append(Lane_H)
                                                            my_Lanes.append(data_rowl)
    Save_to_CSV_lanes(my_Lanes)
    return my_Lanes              




def Match_Lane_Activity(my_Lanes, my_Activities):
    my_Lanes_Activity = []

    for i in range(len(my_Lanes)):
        Lane_Activity_data_rowl = [my_Lanes[i][0]]
        for j in range(len(my_Activities)):
            if (int(my_Activities[j][3]) < int(my_Lanes[i][3]) + int(my_Lanes[i][4]) 
                    and int(my_Activities[j][3]) > int(my_Lanes[i][3])):
                Lane_Activity_data_rowl.append(my_Activities[j][0])
        my_Lanes_Activity.append(Lane_Activity_data_rowl)

    Save_to_CSV_lanes_Activity(my_Lanes_Activity)
    return my_Lanes_Activity
    
def Save_to_CSV_lanes_Activity(my_Lanes_Activity):
        # open the file in the write mode
        f = open('The_extracted_Lanes_Activity.csv', 'w', newline='')
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(["Lane_Name", "Activity_Name"])
        # write multiple rows
        writer.writerows(my_Lanes_Activity)
        # close the file
        f.close()
   



def Save_to_CSV_lanes(my_Lanes):
      # open the file in the write mode
        f = open('The_extracted_Lanes.csv', 'w')
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(["Lane_Name", "Lane_Id", "Lane_X", "Lane_Y", "Lane_H"])
        # write multiple rows
        writer.writerows(my_Lanes)
        # close the file
        f.close()
        
    
def Save_to_CSV_Activities(my_Activities):
    # open the file in the write mode
    f = open('The_extracted_Activities.csv', 'w')
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow(["Activity_Name", "Activity_Id", "X", "Y"])
    # write multiple rows
    writer.writerows(my_Activities)
    # close the file
    f.close()                                              


def main():    
    xpdl_file_path = "Medical2.xpdl"
    tree = ET.parse(xpdl_file_path)
    root = tree.getroot()
    my_Activities = []
    my_Pools =[]
    my_Lanes=[]
    Extract_Activities(root, my_Activities)
    Extract_Lanes(root,my_Lanes)
    Match_Lane_Activity(my_Lanes,my_Activities)

if __name__ == "__main__":
    main()