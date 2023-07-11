# This script will:
# 1. loop through all SUBDIRECTORIES in the CURRENT DIRECTORY 
# 2. loop through all the files
# 3. check if their extensions match {formats}
# 4. convert each file to 320kbs mp3 with ffmpeg OVERWRITING if the file already exists 
# 5. remove the original file
# while logging stuff to ./converted.txt

import datetime
import os
import ffmpeg

# add more formats if you want
formats = ["wav", "m4a", "flac"]

input(f"Read what this script does. Hit return to continue.")

# just for the sake of keeping the logs organized
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("converted.txt", "a") as f: 
        f.write(f"########## {timestamp}\n")

# get all subdirectories and loop through them
for subdir in os.listdir():

    if os.path.isdir(subdir):
        print(f"Entering {subdir}...")
        with open("converted.txt", "a") as f: 
                f.write(f"### {subdir}\n")
       
        # get all files in the subdir and loop through them        
        for file in os.listdir(subdir):

            # get the ext
            extension = file.split(".")[-1]

            # if the file extension is in the list of formats, convert it to mp3
            if extension in formats:
                # get file name w/o extension, split(".")[-1] doesnt work if there are dots in the filename (e.g. "01. Ghosts 'n' Stuff.wav") 
                name = file.rsplit(".",1)[0]

                print(f"Converting {file} to mp3...")
                # convert it to mp3 @ 320kbps, overwrite if file already exists
                stream = ffmpeg.input(f"{subdir}/{file}")
                stream = ffmpeg.output(stream, f"{subdir}/{name}.mp3", audio_bitrate=320000)
                stream = ffmpeg.overwrite_output(stream)

                ffmpeg.run(stream)

                # log affected files to a text file
                with open("converted.txt", "a") as f: 
                    f.write(f"{file}\n--> {name}.mp3\n")

                # remove the original file
                print(f"Removing {file}...")
                os.remove(f"{subdir}/{file}")