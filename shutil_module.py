import shutil
import os
shutil.copy("time_module.py","hello.txt")    # The copy methods copyt the content of a file into another
os.mkdir('Hello')
with open('Hello\\hello.txt','w') as file:
    for i in range(10):
        file.write('This is a file\n')

shutil.copytree('Hello','TimePass')   #The copytree method copy the content of a folder into another


shutil.move('Hello\\class_methods.py','class_methods.py') # This method move file from one destination to another

shutil.rmtree('Hello')  #This method is used to delete a folder







