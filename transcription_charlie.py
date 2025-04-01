import whisper
import os

print("🚀 Starting program...")

def transcribe_audio(audio_path):
    # Check if input file exists
    if not os.path.exists(audio_path):
        print(f"❌ Error: Input file not found at: {audio_path}")
        return

    print(f"📂 Found input file at: {audio_path}")
    
    # Get the video filename without extension
    video_name = os.path.basename(audio_path)
    video_name_no_ext = os.path.splitext(video_name)[0]
    output_dir = os.path.dirname(audio_path)
    
    print(f"🔄 Loading Whisper model...")
    # Initialize Whisper
    try:
        model = whisper.load_model("base")
    except Exception as e:
        print(f"❌ Error loading Whisper model: {e}")
        return

    print(f"🎯 Starting transcription... This may take several minutes.")
    print("💭 Whisper is processing your file. Please wait...")
    # Transcribe the audio
    try:
        result = model.transcribe(audio_path)
    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        return

    # Save the transcription in the same folder as the video
    output_path = os.path.join(output_dir, f"{video_name_no_ext}_transcription.txt")
    print(f"💾 Attempting to save transcription to: {output_path}")
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                # Convert seconds to HH:MM:SS format
                start_time = segment["start"]
                end_time = segment["end"]
                
                start_hrs = int(start_time // 3600)
                start_mins = int((start_time % 3600) // 60)
                start_secs = int(start_time % 60)
                
                end_hrs = int(end_time // 3600)
                end_mins = int((end_time % 3600) // 60)
                end_secs = int(end_time % 60)
                
                # Format with or without leading zeros for hours based on if it's needed
                start_stamp = f"{start_hrs}:{start_mins:02d}:{start_secs:02d}"
                end_stamp = f"{end_hrs}:{end_mins:02d}:{end_secs:02d}"
                
                text = segment["text"]
                f.write(f"\n[{start_stamp} - {end_stamp}]: {text.strip()}\n")
    except Exception as e:
        print(f"❌ Error saving transcription: {e}")
        return

    print(f"✅ Transcription saved to: {output_path}")


# Example usage
if __name__ == "__main__":
    print("📌 Program reached main section")
    audio_file = "/Users/charlottelau/Documents/LTAIT/transcript/meeting.mp4"
    transcribe_audio(audio_file) 
