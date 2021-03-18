'''
Inserts a one page pdf into another pdf in a certain position
'''

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os
import glob
from subprocess import check_call
import shutil

# Get list of files to be inserted (1 page each)
pages_list = os.listdir("C:/Users/phant/Desktop/Page Inserts")
os.chdir("C:/Users/phant/Desktop/Page Inserts")

# Loop over pages to be inserted
for page in pages_list:
    # Open insert file
    finsert = open(page, 'rb')
    pdfinsert = PdfFileReader(finsert)

    # Force decrypt the file
    if pdfinsert.isEncrypted:
        try:
            pdfinsert.decrypt('')
            print('File Decrypted (PyPDF2)')
        except:
            check_call(['qpdf', "--password=", '--decrypt', page, "temp.pdf"])
            shutil.move("temp.pdf", page)
            finsert = open(page, 'rb')
            pdfinsert = PdfFileReader(finsert)    

    # Split the page name to get the insert page number and the doc name
    num, fname = page.split(' ', 1)

    # Find the doc by searching recursively in self study
    path = "C:/Users/phant/Desktop/Self Study"

    # Find the location of the file to be updated
    fin = False
    for root, dirs, files in os.walk(path):
        for f in files:
            if f == fname:
                file = f
                fin = True
                break
        if fin:
            break

    # Open the file to be updated
    f = open(root + "/" + file, 'rb')
    pdf = PdfFileReader(f)
    
    # Force decrypt the file
    if pdf.isEncrypted:
        try:
            pdf.decrypt('')
            print('File Decrypted (PyPDF2)')
        except:
            check_call(['qpdf', "--password=", '--decrypt', root + "/" + file, "temp.pdf"])
            shutil.move("temp.pdf", root + "/" + file)
            f = open(root + "/" + file, 'rb')
            pdf = PdfFileReader(f)
    
    # Loop over file to be updated, add those pages into the writer object 
    # except for the num page, for which the page to be inserted is added
    length = pdf.getNumPages()
    pdf_writer = PdfFileWriter()
    for p in range(length):
        if p == int(num) - 1:
            pdf_writer.addPage(pdfinsert.getPage(0))
        else:
            pdf_writer.addPage(pdf.getPage(p))

    # Write the new pdf to out.pdf
    with open("out.pdf", 'wb') as out:
        pdf_writer.write(out)

    # Close the two files
    f.close()
    finsert.close()

    # Find how many backups there are to see what suffix to add
    files = os.listdir("D:/Page Inserts Backup/")
    files = [i for i in files if page.replace(".pdf","") in i]

    # Copy the page just inserted to the backups directory
    command1 = "copy " + "\"" + page + "\"" + " \"D:/Page Inserts Backup/" + page.replace(".pdf","") + " " + str(len(files)+1) + ".pdf\""
    command2 = "copy out.pdf " + "\"" + root + "/" + file + "\""
    os.system(command1)
    os.system(command2)

    # Remove the insert page and out.pdf
    os.remove(page)
    os.remove("out.pdf")

    print(f"SUCCESS: {page}")
