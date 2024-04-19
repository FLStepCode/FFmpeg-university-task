import os
import sys
import media_processor
import media_merger

consent = ""

while consent != "y":
    print("Warning!!! If the script is executed, contents in the folder 'Output' will be wiped!")
    print("Do you want to continue? [y / n]", end=' ')
    consent = input()
    if consent == "n":
        sys.exit()

with os.scandir("Container") as media:

    for file in media:
        if file.name != ".gitignore":
            os.remove(file)


with os.scandir("Source") as media:

    counter = 0
    audio_flag = 0

    for file in media:

        name = file.name.split(".")

        if name[len(name) - 1] in ["mp4", "jpg", "mp3"]:

            if name[len(name) - 1] == "mp4":
                counter += 1
                media_processor.trim_video(file.name, counter)
            elif name[len(name) - 1] == "jpg":
                counter += 1
                media_processor.transfer_images(file.name, counter)
            elif name[len(name) - 1] == "mp3":
                audio_flag = 1
                media_processor.transfer_audio(file.name)


with os.scandir("Output") as media:

    for file in media:
        if file.name != ".gitignore":
            os.remove(file)


if counter != 0 and audio_flag == 1:
    print("Merging...")
    media_merger.merge()
    print("\nMerged successfully into out.mp4 in 'Output' folder!")
elif audio_flag == 0 and counter != 0:
    print("No audio!")
    sys.exit()
elif audio_flag == 1 and counter == 0:
    print("No video!")
    sys.exit()
else:
    print("No audio! No video!")
    sys.exit()

print("Cleaning up the folder 'Container'...")
with os.scandir("Container") as media:

    for file in media:
        if file.name != ".gitignore":
            os.remove(file)
print("Finished!")
