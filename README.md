# pdf_note_tool
Tool to allow note taking in pdfs through inserting scanned pages since I didn't want to pay for Evernote or Acrobat.

## init.py

Takes all pdfs from the intake directory and for each inserts alternating blank pages. These pages can then later be updated with scanned pdfs of handwritten notes or pdfs of typed notes using insert.py. These pdfs are then moved to the root pdf storage directory to be sorted based on their topic.

## insert.py

Takes all insert pages from the insert directory ("Page Inserts") and for each find the corresponding file and insert the page into it. Insert pages are identified with file names of the format "{num} {target file name}" where "num" is the number of the page for the insert page to be inserted to and "target file name" is the name of the file for it to be inserted into.

## Path

On Windows you can run these scripts from the command line without specifying the directory by adding the directory containing init.py and insert.py to the PATH variable.
