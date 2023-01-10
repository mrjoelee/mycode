#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Copying Files and Folder """

#import additional code to complete the task
import shutil 
import os

def main():
    """runtime"""
    
    #allow the user to run the program any location on the system
    os.chdir("/home/student/mycode/")

    #copy the file at the path source to the folder at the path destination
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    #copy an entire folder and every folder and file contained in it. 
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")
    
if __name__ == "__main__":
    main()

