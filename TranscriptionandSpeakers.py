import whisper
from pyannote.audio import Pipeline
import torch
import os
import ssl
from pydub import AudioSegment

ssl._create_default_https_context = ssl._create_unverified_context


def convert_mp4_to_wav(mp4_path):
    """Convert MP4 to WAV format"""
    wav_path = mp4_path.rsplit('.', 1)[0] + '.wav'
    audio = AudioSegment.from_file(mp4_path, format="mp4")
    audio.export(wav_path, format="wav")
    return wav_path


def transcribe_with_speakers(audio_path, output_dir, speaker_names=None):
    # Convert MP4 to WAV if necessary
    if audio_path.lower().endswith('.mp4'):
        audio_path = convert_mp4_to_wav(audio_path)

    # Initialize Whisper
    model = whisper.load_model("base")

    # Initialize Pyannote pipeline
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization",
        use_auth_token="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"
    )

    # Perform diarization
    diarization = pipeline(audio_path)

    # Transcribe the audio
    result = model.transcribe(audio_path)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a mapping of speaker labels to names if provided
    speaker_map = {}
    if speaker_names:
        unique_speakers = set()
        # First pass to collect unique speakers
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            unique_speakers.add(speaker)

        # Map speakers to provided names
        for i, speaker in enumerate(sorted(unique_speakers)):
            if i < len(speaker_names):
                speaker_map[speaker] = speaker_names[i]
            else:
                speaker_map[speaker] = f"SPEAKER_{speaker}"

    # Write the output
    output_path = os.path.join(output_dir, "transcription_with_speakers.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            start_time = turn.start
            end_time = turn.end

            # Use mapped name if available, otherwise use default speaker label
            speaker_name = speaker_map.get(speaker, f"SPEAKER_{speaker}")

            # Find matching transcription
            matching_segments = [s for s in result["segments"]
                                 if s["start"] <= end_time and s["end"] >= start_time]

            for match in matching_segments:
                f.write(f"\n{speaker_name} ({start_time:.1f}s - {end_time:.1f}s):\n")
                f.write(f"{match['text'].strip()}\n")


# Example usage
if __name__ == "__main__":
    # Replace these paths with your actual paths
    audio_file = "/Users/Amos/Downloads/test_short.mp4"  # Using the shorter test file
    output_directory = "/Users/Amos/transcripts/output"

    # Updated speakers list for Charlie and Netta
    speakers = ["Charlie", "Netta"]

    transcribe_with_speakers(audio_file, output_directory, speakers)