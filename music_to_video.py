import subprocess
import argparse
import os

def create_video(image_path, audio_path, output_path, resolution=(1920, 1080), compress_audio=False):
    # Check files' existence
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file is not found: {image_path}")
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Audio file is not found: {audio_path}")
    
    width, height = resolution
    aspect_ratio = f"{width}/{height}"
    audio_codec = "aac" if compress_audio else "copy"

    # FFmpeg command
    command = [
        "ffmpeg",
        "-loop", "1", 
        "-i", image_path,
        "-i", audio_path,
        "-vf", f"scale='if(gt(iw/ih, {aspect_ratio}), {width}, -1)':'if(gt(iw/ih, {aspect_ratio}), -1, {height})',pad={width}:{height}:(ow-iw)/2:(oh-ih/2)",
        "-c:v", "libx264", # video codec
        "-preset", "slow", # encoding preset
        "-crf", "18", # quality
        "-c:a", audio_codec, # audio codec (aac for compressed audio)
        "-b:a", "192k", # audio bitrate
        "-pix_fmt", "yuv420p", # pixel format
        "-shortest", # match video duration to audio
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Video created successfully:  {output_path}")
    except subprocess.CalledProcessError as e:
        print("Error occured white creating video:", e)
        
def main():
    parser = argparse.ArgumentParser(description="Create a simple, static video with a cover and audio file.")
    parser.add_argument("--image", "-i", required=True, help="Path to the cover image.")
    parser.add_argument("--audio", "-a", required=True, help="Path to the audio file.")
    parser.add_argument("--output", "-o", default="output.mp4", help="Path to the output file.")
    parser.add_argument("--resolution", "-r", default="1920x1080", help="Resolution of the output video (e.g., 1920x1080).")
    parser.add_argument("--compress-audio", "-c", action="store_true", help="Compress audio to AAC (default: copy original audio).")
    
    args = parser.parse_args()

    try:
        width, height = map(int, args.resolution.split('x'))
        resolution = (width, height)
    except ValueError:
        print("Invalid resolution. Use WIDTHxHEIGHT")
    
    create_video(args.image, args.audio, args.output, resolution, args.compress_audio)

if __name__ == "__main__":
    main()