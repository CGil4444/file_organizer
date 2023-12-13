import os
import shutil
import sys

def make_folders(path,categories):
    #creating folders for each category
    for category in categories:
        new_path = os.path.join(path,category)
        os.makedirs(new_path,exist_ok=True)
    
    #making an "Other" folder for any other filetypes not addressed
    other_path = os.path.join(path,"Other")
    os.makedirs(other_path,exist_ok=True)
    
def organize_files(path):
    #For sorting based on file extensions
    categories = {
        "Videos" : ['.mp4','.mov','.avi','.wmv','.flv','.webm','.mkv','.mpeg','.mpg','.3gp','.m4v'],
        "Images" : ['.png','.jpg','.jpeg','.gif','.bmp','.tiff','.webp','.svg','.ico','.psd','.swf'],
        "Documents" : ['.pdf','.7z','.txt','.doc','.docx','.pptx','.ppt','.xls','.csv','.html','.xlsx','.stl','.epub','.tex','.zip','.rar','.iso'],
        "Audio" : ['.mp3','.aac','.m4a','.wav','.ogg','.flac','.aiff','.aif','.wma'],
        "Code":['.exe','.jar','.java','.js','.class','.h','.c','.cpp','.py','.msi','.unity','.unitypackage','.apk','.dll','.mid']
    }
    #making folders to organize files in
    make_folders(path,categories.keys())

    #iterating through each file in the root dir
    for filename in os.listdir(path):
        for category in categories:#iterating through each category in the dict
            extension = os.path.splitext(filename)[1] #getting extension of current file
            source = os.path.join(path,filename) #creating current file absolute path
            if extension in categories.get(category): #if match found, move file into corresponding category folder
                destination = os.path.join(path,category,filename)
                #(f"Moving {source} to {destination}") #use for debugging purposes
                shutil.move(source,destination)
        #in case a file doesn't match a known extension, move it to the 'Other' folder
        if os.path.exists(source) and os.path.isfile(source):
            destination = os.path.join(path,"Other",filename)
            #(f"Moving {source} to {destination}") #use for debugging purposes
            shutil.move(source,destination)
    print("Finished organizing!")
    return True

path = input("Enter an absolute path to organize: ")
if os.path.exists(path) != True:
    print(f"Could not find path '{path}'",file=sys.stderr)
    exit(1)
organize_files(path)
