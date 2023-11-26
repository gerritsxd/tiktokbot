from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Load the video
video = VideoFileClip('output_folder/tiktok_video.mp4')

# Load and parse the SRT subtitle file
subtitles = []
with open('subtitle.srt', 'r') as subtitle_file:
    lines = subtitle_file.read().split('\n\n')
    for line in lines:
        linesplit = line.split('\n')
        timing = linesplit[1]
        text = '\n'.join(linesplit[2:])
        subtitles.append((timing, text))

# Create TextClip objects for each subtitle
subtitle_clips = []
for timing, text in subtitles:
    subtitle_clip = TextClip(text, fontsize=24, color='white')
    subtitle_clip = subtitle_clip.set_duration(video.duration)  # Set duration to match video
    subtitle_clip = subtitle_clip.set_start(timing)  # Set start time using subtitle timing
    subtitle_clips.append(subtitle_clip)

# Composite video with subtitles
video_with_subtitles = CompositeVideoClip([video] + subtitle_clips)

# Save the final video with subtitles
video_with_subtitles.write_videofile('output_folder/final_video_with_subtitles.mp4')
