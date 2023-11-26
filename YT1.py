from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Function to download a YouTube video and crop it
def download_and_crop_video(url, start_time, end_time, output_path):
    # Download the YouTube video
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

    # Crop the video using moviepy
    input_video = output_path + '/' + yt.title + '.mp4'
    ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_path + '/cropped_video.mp4')

# URLs of the YouTube videos
url1 = 'https://www.youtube.com/watch?v=VIDEO1_ID'
url2 = 'https://www.youtube.com/watch?v=VIDEO2_ID'

# Define crop time intervals (in seconds)
start_time1, end_time1 = 60, 600  # Adjust as needed
start_time2, end_time2 = 120, 720  # Adjust as needed

# Output folder
output_folder = 'output_folder'  # Change to your desired folder path

# Download and crop the videos
download_and_crop_video(url1, start_time1, end_time1, output_folder)
download_and_crop_video(url2, start_time2, end_time2, output_folder)
