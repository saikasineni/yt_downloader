import yt_dlp
import pygame
import threading

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")  # your background music file
    pygame.mixer.music.play(-1)  # -1 = loop forever

def stop_music():
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def download_yt_video(url):
    ydl_opts = {
        'format': 'best[height<=1080]',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")

    # Start music in separate thread
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

    download_yt_video(video_url)

    stop_music()