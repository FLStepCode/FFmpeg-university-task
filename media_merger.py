import os
import subprocess


def merge():

    command = ["ffmpeg"]
    audio = ""

    with os.scandir("Container") as media:

        counter = 0

        for file in media:
            name = file.name.split('.')
            if name[len(name) - 1] == "jpg":
                piece = ["-loop", "1",
                         "-framerate", "60",
                         "-t", "2",
                         "-i", f"Container/{file.name}"]
                command += piece
                counter += 1
            elif name[len(name) - 1] == "mp4":
                piece = ["-i", f"Container/{file.name}"]
                command += piece
                counter += 1
            elif name[len(name) - 1] == "mp3":
                audio = file.name

    complex_filter = ""
    for i in range(counter):
        complex_filter += f"[{i}]"
    complex_filter += f"concat=n={counter}:v=1:a=0"
    command += ["-filter_complex", complex_filter, "Container/out_an.mp4"]

    subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    subprocess.call([
        "ffmpeg",
        "-i", "Container/out_an.mp4",
        "-i", f"Container/{audio}",
        "-filter:a", "volume=0.5",
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "copy",
        "-shortest", "Output/out.mp4"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
