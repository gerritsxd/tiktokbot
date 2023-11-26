from moviepy.editor import VideoFileClip, clips_array

# Load the cropped videos
video1 = VideoFileClip('output_folder/cropped_video1.mp4')
video2 = VideoFileClip('output_folder/cropped_video2.mp4')

# Combine the videos side by side
final_video = clips_array([[video1, video2]])

# Save the combined video in TikTok format
final_video.write_videofile('output_folder/tiktok_video.mp4')
