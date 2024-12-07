# **Music to Video Converter**

A lightweight Python tool to create video from a static image and an audio file. It is for turning music tracks and cover art into videos for platforms like YouTube.

## **Usage**

1. **Install Dependencies**:
   - Install FFmpeg:
     - **macOS**: `brew install ffmpeg`
     - **Linux**: `sudo apt install ffmpeg`
     - **Windows**: Download and install from [FFmpeg.org](https://ffmpeg.org/download.html).

2. **Run the Script**:
   ```bash
   python music_to_video.py --image <path_to_image> --audio <path_to_audio> [OPTIONS]

### **Options**
- `--image` or `-i`: Path to the image file (e.g., `cover.png`).
- `--audio` or `-a`: Path to the audio file (e.g., `song.wav`).
- `--output` or `-o`: Output video file path (default: `output.mp4`).
- `--resolution` or `-r`: Video resolution (default: `1920x1080`).
- `--compress-audio` or `-c`: Compress audio to AAC format (default: lossless).
