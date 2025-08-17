from pydub import AudioSegment
import os
from pydub.utils import which

def convert_video_to_audio(video_path: str, output_format="wav") -> str:
    """
    Converts a video file to an audio file using pydub.
    """
    # Check if FFmpeg is available
    ffmpeg_path = which("ffmpeg")
    if not ffmpeg_path:
        raise EnvironmentError("FFmpeg is not installed or not found in PATH.")

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file {video_path} not found.")

    # Define the output path
    audio_output_path = f"{os.path.splitext(video_path)[0]}.{output_format}"

    # Convert video to audio
    audio = AudioSegment.from_file(video_path, format="mp4")  # Specify format if necessary
    audio.export(audio_output_path, format=output_format)

    return audio_output_path
