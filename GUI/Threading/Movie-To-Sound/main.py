#### MohammadAli Mirzaei ####

import time
from threading import Thread
import requests 
from moviepy import editor
import os

def download_video(url, file_name):
    """
    Function to download a video from a given URL and save it to a file.
    """
    try:
        # Send request to download the video
        result = requests.get(url)
        # Write the content to a file
        with open(file_name, "wb") as f:
            f.write(result.content)
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def convert_video_to_audio(index, video_file):
    """
    Function to convert a video file to an audio file.
    """
    try:
        # Load the video file
        video_clip = editor.VideoFileClip(video_file)
        # Extract audio and save it to a file
        video_clip.audio.write_audiofile(f"audio/audio{index + 1}.mp3")
    except Exception as e:
        print(f"Error converting {video_file} to audio: {e}")

def normal_execution():
    """
    Function to perform video to audio conversion without multithreading.
    """
    start_time = time.time()
    for i in range(1, 6):
        # Convert each video to audio sequentially
        video_clip = editor.VideoFileClip(f"output/video{i}.mp4")
        video_clip.audio.write_audiofile(f"output/audio{i}.mp3")
    end_time = time.time()
    print(f"\nDuration of normal conversion: {end_time - start_time} seconds.\n")

def multi_threading_execution():
    """
    Function to perform video to audio conversion with multithreading.
    """
    start_time = time.time()
    threads = []
    for index, file in enumerate(output_files):      
        # Create a thread for each video conversion task
        thread = Thread(target=convert_video_to_audio, args=[index, file])
        threads.append(thread)
        # Start the thread
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"\nDuration of multithreaded conversion: {end_time - start_time} seconds.\n")

if __name__ == "__main__":
    # Ensure directories exist for output files
    if not os.path.exists("output"):
        os.makedirs("output")
    if not os.path.exists("audio"):
        os.makedirs("audio")

    # List of video URLs
    video_urls = [ "https://aspb15.cdn.asset.aparat.com/aparat-video/00704eb4d3f5ec4600ef1f47767ddd7f14028226-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjMzODViZTRmODE4NDAyYTRmZjc3NWU4NjhjYjZmNjM5IiwiZXhwIjoxNjc4NzIyMDU3LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.CscwAqFd9pSMCABfmIaqlmDHghKsdT-C_VNYIEUH94Q" ,
           "https://aspb3.cdn.asset.aparat.com/aparat-video/59502de31f677be549ad5dc2c9a639f014143770-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjA0OWE5NTA0M2I1ZmMzMDMyOTE2OThkN2JjMmVmYTZlIiwiZXhwIjoxNjc4NzIxODcwLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.YWhWqxyhLNzwTBQfXxth1evrJksebxWjYWEPae1LI64" ,
           "https://aspb3.cdn.asset.aparat.com/aparat-video/71a25cb7bf41a749a92c127b19b7f63910411185-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjRlNTQyNTQyODc3YmQ4MmUzMGE5ZmNhYjYxNzU0ODMxIiwiZXhwIjoxNjc4NzIyMTY1LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.ixCOAcyP08QN9Hmg6p30wzeShQX8moc11Tf2YRh30_I" ,
           "https://aspb11.cdn.asset.aparat.com/aparat-video/5521fe3e0d12c444101acc05468c5e7514605620-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjNhMWEwOTZmMzQyOTdjZWExZGQ3ZDc2ZjAwODM4ZWY5IiwiZXhwIjoxNjc4NzIyMjQwLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.HJLpuLobk2S9XrF2zb-6XUGlJ7baoSPZqcBmLAB48ng" ,
           "https://as10.cdn.asset.aparat.com/aparat-video/a3672b5779abfaf20d257214a61fd4088244946-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjcxMjBmZmQ3NTZmYjhlZDM1MTUyY2UyYjUwOTE0ZjAzIiwiZXhwIjoxNjc4NzIyODU2LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.bA2SeyJjaY6Ic-HgbFpW50y3QTT8KOYN1_8ul0yRD84" ]

    # Download videos from URLs
    output_files = []
    for i, url in enumerate(video_urls):
        download_video(url, f"output/video{i+1}.mp4")
        output_files.append(f"output/video{i+1}.mp4")

    # Perform video to audio conversion
    normal_execution()
    multi_threading_execution()
