from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os


def convertName(text):
    workingtext = text.replace(" ", "")
    textlist = list(workingtext)
    for i in range(0, len(textlist)):
        if not ((65 <= ord(textlist[i]) <= 90) or (97 <= ord(textlist[i]) <= 122)):
            textlist[i] = "_"
    return "".join(textlist)


media_type = int(
    input("How would you like to download the Video(s)?\nSingle Video: 0\nPlaylist: 1\nSingle Videos from File: 2\n"))

url = input("Enter YouTube URL:- ")

if media_type == 1:

    p = Playlist(url)
    for video in p.videos:
        highresvid = video.streams.filter(file_extension="mp4").get_highest_resolution()
        videoName = convertName(video.title)
        highresvid.download('conversion', filename=(videoName + ".mp4"))
        mp4_file = "conversion\\" + videoName + ".mp4"
        mp3_file = "conversion\\" + videoName + ".mp3"

        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()

        os.remove("conversion\\" + videoName + ".mp4")
elif media_type == 0:
    video = YouTube(url)
    highresvid = video.streams.filter(file_extension="mp4").get_highest_resolution()
    videoName = convertName(video.title)
    highresvid.download('conversion', filename=(videoName + ".mp4"))

    mp4_file = "conversion\\" + videoName + ".mp4"
    mp3_file = "conversion\\" + videoName + ".mp3"

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()

    os.remove("conversion\\" + videoName + ".mp4")
elif media_type == 2:

    with open(url) as f:
        urls = [line.rstrip('\n') for line in f]

    for vid_url in urls:
        video = YouTube(vid_url)
        highresvid = video.streams.filter(file_extension="mp4").get_highest_resolution()
        videoName = convertName(video.title)
        highresvid.download('conversion', filename=(videoName + ".mp4"))
        mp4_file = "conversion\\" + videoName + ".mp4"
        mp3_file = "conversion\\" + videoName + ".mp3"

        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()

        os.remove("conversion\\" + videoName + ".mp4")
