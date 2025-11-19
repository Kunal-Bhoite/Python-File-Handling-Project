from pathlib import Path
import os

def all_files_in_folder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items}")

def create_a_file():
    all_files_in_folder()
    try:
        name=input("Enter the name of your file:") 
        p=Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data=input("what do you want to write:")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY..!")
        else:
            print("File Already Exists..!")

    except Exception as err:
        print(f"An Error Occured as {err}")


def read_file():
    all_files_in_folder()
    try:
        name=input("Which File Do you want to read:")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            
            print("FILE READED SUCCESSFULLY..!")
        else:
            print(f"File Does Not Exist..!")
        
    except Exception as err:
        print(f"An Error Occured as {err} ")



def update_file():
    all_files_in_folder()
    try:
        name=input("Enter the file you want to Update")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 to RENAME the file:")
            print("Press 2 to OVERWRITE the file:")
            print("Press 3 to APPEND the file:")

            res=int(input("Please choose an option:"))
            if res==1:
                name2=input("Enter a New Name for a file you want to Rename:")
                p2=Path(name2)
                p.rename(p2)
                print("RENAME is Successfull..!")
            if res==2:
                with open(p,'w') as fs:
                    data=input("Tell what you want to write **This will be Overwritten**")
                    fs.write(data)
                    print("OVERWRITE is Successfull..!")
            if res==3:
                with open(p,'a') as fs:
                    data=input("Tell what you want to Append")
                    fs.write(" "+data)
                    print("APPEND is Successfull..!")
    except Exception as err:
        print("An Error Occured as {err}")

def delete_file():
    try:
        name=input("Enter the file you want to Delete:")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(name)

            print("File Deleted Successfully..!")
        else:
            print("File Does Not Exist..!")
    except Exception as err:
        print(f"An Error Occured as {err}")






print("Press 1 to Create a File")
print("Press 2 to Read a File")
print("Press 3 to Update a File")
print("Press 4 to Delete a File")

check=int(input("Please choose an option:"))
if check ==1:
    create_a_file()
if check==2:
    read_file()
if check ==3:
    update_file()
if check==4:
    delete_file()