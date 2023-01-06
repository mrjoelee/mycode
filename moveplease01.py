#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Moving and Renaming Files and Folders """

#importing additional to complete task
import shutil
import os

def main():
    """runtime"""

    #run the program from any location on the system
    os.chdir('/home/student/mycode/')

    #move the file or folder at the path source to the path destination
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompt user for a new name for the file
    xname = input('What is the new name for kerrigan.obj? ')
    
    #rename the file with the user input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
    
if __name__ == "__main__":
    main()
