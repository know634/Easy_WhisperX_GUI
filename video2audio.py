# -- coding: utf-8 --
from moviepy.editor import VideoFileClip

# 视频文件路径
video_file = r"C:\Users\XGR\Desktop\SoftwareDev\008字幕识别小工具\test\test.mp4"
# 输出音频文件路径
audio_file = r"C:\Users\XGR\Desktop\SoftwareDev\008字幕识别小工具\test\test.mp3"

# 加载视频文件
clip = VideoFileClip(video_file)

# 提取音频
audio = clip.audio

# 写入音频到文件
audio.write_audiofile(audio_file, codec='mp3')

# 清理资源
audio.close()
clip.close()
