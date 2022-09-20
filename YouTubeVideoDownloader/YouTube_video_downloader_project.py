#youtube download project
import sys
from pytube import YouTube
import pywhatkit

#taking link as input
link=input("enter the link:")

#plays the video online
pywhatkit.playonyt(link)

video=YouTube(link)

#printing the title and views of the video
print("Title:",video.title)

print("Views:",video.views)

#asking user for resolution
print("1. For low resolution")
print("2. For high resolution")
print("3. Enter resolution")
ask_reso=int(input("Enter your choice:"))
if ask_reso==1:
    video_download=video.streams.get_lowest_resolution()
if ask_reso==2:    
    video_download=video.streams.get_highest_resolution()
if ask_reso==3:
    reso=input("Enter resolution(For Eg.-240p/360p/etc.):")
    video_download=video.streams.get_by_resolution(str(reso))

#providing the download folder 
video_download.download("C:\\Users\\jeeva\\OneDrive\\Desktop\\Python\\Python Projects")
