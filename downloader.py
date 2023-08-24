from pytube import YouTube 
from pytube.exceptions import RegexMatchError
from pytube.exceptions import AgeRestrictedError

print("\n --- Welcome to Youtube Downloader 🎥 ---\n")
link = input("Please insert a valid Youtube link: ")

try:
    video = YouTube(link)
    print("\nDownloading ", video.title,)
    print("Number of views: ", video.views)
    video = video.streams.get_highest_resolution()
    video.download("./downloaded_videos")
    print("Video 100% downloaded")
except RegexMatchError:
    print("Invalid YouTube link. Please provide a valid link.")
except AgeRestrictedError:
    print("Video is age restricted, and cannot be accessed without authentication.")