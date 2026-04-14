#!/usr/bin/python

import base64
import json
import os
import sys

folder_path1 = str(sys.argv[1])
folder_path = folder_path1 + '/jsonOut'
print (folder_path)

filenames = []

for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and file_path.endswith('.json'):
            filenames.append(file_path)

            print (f"File: " +filename)

#print (str(filenames))

print ("Total Emails with Attachments = " + str(len(filenames)))


base_out_dir = folder_path1 + '/attachmentStore'


for file in filenames:
    print ("Converting " + file)
    with open( file, 'rb' ) as jsonfile:
        
         record = json.load(jsonfile)
        
         print ("Number of Attached Files in this Email: " +str(len(record['result'])))
            
         for k in range (len(record['result'])):
            #print (record['result'][k]['ATT_NAME'])
            fname = (record['result'][k]['ATT_NAME'])
            full_filename = os.path.join(base_out_dir,fname)
            print ("Generating " + fname)

            with open(full_filename, 'wb') as output:
                output.write(base64.b64decode(record['result'][k]['CONTENT']))
