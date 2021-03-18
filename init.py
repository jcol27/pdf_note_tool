'''
Sets up all pdfs in the intake directory for note 
taking by adding blank pages every other page
'''

import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from subprocess import check_call
import shutil

files_list = os.listdir("C:/Users/phant/Desktop/Pdf Temp")
os.chdir("C:/Users/phant/Desktop/Pdf Temp")

# Loop over all files in the intake directory
for file in files_list:
    # Open the file
    f = open(file, 'rb')
    pdf = PdfFileReader(f)
    
    # Force decrypt the file
    if pdf.isEncrypted:
        try:
            pdf.decrypt('')
            print('File Decrypted (PyPDF2)')
        except:
            check_call(['qpdf', "--password=", '--decrypt', file, "temp.pdf"])
            shutil.move("temp.pdf", file)
            f = open("C:/Users/phant/Desktop/Pdf Temp/" + file, 'rb')
            pdf = PdfFileReader(f)
    
    # Loop through the file and create a new pdf with alternating blank pages
    length = pdf.getNumPages()
    pdf_writer = PdfFileWriter()
    for page in range(length):
        pdf_writer.addPage(pdf.getPage(page))
        pdf_writer.addBlankPage()
    
    # Write this new file to out.pdf
    with open("out.pdf", 'wb') as out:
        pdf_writer.write(out)

    # Close the file
    f.close()

    # Copy the old file to the backup folder, copy the new file to the storage directory to be sorted
    command1 = "copy " + "\"" + file + "\"" + " \"D:/Books Backup/COPY " + file + "\""
    command2 = "copy out.pdf \"C:/Users/phant/Desktop/Self Study/" + file + "\""
    os.system(command1)
    os.system(command2)

    # Remove the old file and out.pdf
    os.remove(file)
    os.remove("out.pdf")

    print(f"SUCCESS: {file}")
