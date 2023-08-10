from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
from pathlib import Path


class Download:
    def __init__(self, url):
        self.url = url
        self.download_folder = self.get_user_download_folder()

    def download_youtube_video(self):
        try:
            yt = YouTube(self.url)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(self.download_folder)
            self.name = str(video_stream.default_filename)
            return video_stream.default_filename

        except Exception as e:
            print("Error:", e)
            return None

    def convert_video_to_mp3(self, video_file):
        try:
            print(video_file)
            video_clip = VideoFileClip(video_file)
            audio_clip = video_clip.audio
            self.output_filename = f"{self.download_folder}/{video_clip.filename.split('.')[0]}.mp3"
            self.video = f"{self.download_folder}/{video_clip.filename.split('.')[0]}.mp4"
            audio_clip.write_audiofile(self.output_filename)
            audio_clip.close()
            video_clip.close()
            return self.output_filename

        except Exception as e:
            print("Error:", e)
            return None

    def get_user_download_folder(self):
        home_dir = str(Path.home())
        if os.name == 'posix':
            download_folder = os.path.join(home_dir, 'Downloads')
        elif os.name == 'nt':
            download_folder = os.path.join(home_dir, 'Downloads')
        else:
            raise OSError("Unsupported operating system")
        return download_folder

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("The specified file does not exist.")
        except PermissionError:
            print("Permission error: You do not have the required permission to delete the file.")
        except Exception as e:
            print(f"An error occurred: {e}")
