import subprocess
import shutil
import cv2


def trim_video(filename, counter):

    print(f"Converting fragment {counter}...")

    cap = cv2.VideoCapture(f"./Source/{filename}")
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = frame_count // fps

    if duration >= 6:
        subprocess.call([
            "ffmpeg",
            "-i", f"Source/{filename}",
            "-ss", "00:00:00",
            "-to", "00:00:06",
            "-filter_complex",
            "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1",
            "-an",
            "-r", "60",
            f"Container/output{counter}.mp4"
        ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)
    else:
        subprocess.call([
            "ffmpeg",
            "-i", f"Source/{filename}",
            "-filter_complex",
            "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1",
            "-an",
            "-r", "60",
            f"Container/output{counter}.mp4"
        ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)


def transfer_images(filename, counter):

    print(f"Converting fragment {counter}...")

    subprocess.call([
        "ffmpeg",
        "-i", f"Source/{filename}",
        "-filter_complex",
        "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1",
        f"Container/output{counter}.jpg"
    ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT)


def transfer_audio(filename):

    shutil.copy(f"Source/{filename}", f"Container/{filename}")
