import os
import classes.file as f

file1 = f.file("ROSE.PNG", 103546, "2023-11-13")

file1.save()

file2 = f.file.create("flowers.css", 6453, "2023-11-13")
file3 = f.file.create("flowers.html", 489, "2023-11-13")
file4 = f.file("posie.png", 203586, "2023-11-11")
file5 = f.file("lily.jpeg", 8234599, "2023-11-11")

files = [file1, file2, file3, file4, file5]

image_extensions = ["jpeg", "jpg", "gif", "png"]

def isImage(file):
    try:
        filename, file_extension = os.path.splitext(file.fileName)
    except SyntaxError:
        # if filename is unicode, we can't work with it, but we don't
        # want to terminate working with the other files
        # we'd rather have it display a message and continue
        print ("File '" + file.fileName + "' contains unicode characters and cannot be processed by this script")
        return False
        
    return file_extension.lower().strip(".") in image_extensions

images = filter(isImage, files)

file_names = list(map(lambda file: file.fileName.lower(), images))

file_names.sort()

for image in file_names:
    print(image)