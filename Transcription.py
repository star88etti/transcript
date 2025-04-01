import whisper
import os


def transcribe_audio(audio_path, output_dir):
    # Get the video filename without extension
    video_name = os.path.basename(audio_path)
    video_name_no_ext = os.path.splitext(video_name)[0]

    # Initialize Whisper
    model = whisper.load_model("base")

    # Transcribe the audio
    result = model.transcribe(audio_path)

    # Save the transcription in the same folder as the video
    output_path = os.path.join(output_dir, f"{video_name_no_ext}_transcription.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"]
            f.write(f"\n[{start_time:.1f}s - {end_time:.1f}s]: {text.strip()}\n")

    print(f"✅ Transcription saved to: {output_path}")


# Example usage
if __name__ == "__main__":
    # Replace these paths with your actual paths
    # audio_file = "/Users/Amos/Downloads/4threcording.mp4"
    audio_file = "/Users/charlottelau/Documents/LTAIT/transcript/meeting.mp4"

    # output_directory = "/Users/Amos/transcripts/output"
    output_directory = "/Users/charlottelau/Documents/LTAIT/transcript/"

    transcribe_audio(audio_file, output_directory)