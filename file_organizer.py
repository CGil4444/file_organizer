import os
import shutil

def organize_files(path):
    #For sorting based on file extensions
    categories = {
        "Videos" : ['.mp4','.mov','.avi','.wmv','flv','webm','mkv','mpeg','mpg','.3gp','m4v'],
        "Images" : ['.png','.jpg','jpeg','.gif','.bmp','.tiff','.webp','.svg','.ico'],
        "Documents" : ['.pdf','.txt','.doc','.docx','.xls','.csv','.html','.xlsx','.stl','.epub','.tex','.zip','.rar','.iso'],
        "Audio" : ['.mp3','.aac','.m4a','.wav','.ogg','.flac','.aiff','.aif','.wma'],
        "Code":['.exe','.jar','.c','.cpp','.py','.msi','.unity','.apk','.dll','.mid']
    }
    #creating folders for each category
    for category in categories.keys():
        if not os.path.exists(path+"\\"+category):
            new_path = path + "\\" + category
            print(f"Creating '{category}' folder")
            os.makedirs(new_path)
    #making the "Other" folder for any other filetypes not addressed
    os.makedirs(path+"\\Other",exist_ok=True)
    for filename in os.listdir(path):
        for category in categories:
            extension = os.path.splitext(filename)[1]
            source = os.path.join(path,filename)
            if extension in categories.get(category):
                destination = os.path.join(path,category,filename)
                shutil.move(source,destination)
            #else: this is still a WIP bc it doesnt work properly lol
                #destination = os.path.join(path,"Other",filename)
                #shutil.move(source,destination)


    return True

path = input()
if os.path.exists(path) != True:
    print("Could not find path '{path}'")
    exit(1)
organize_files(path)
