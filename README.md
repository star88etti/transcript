# How to Transcribe Your Meeting

## Step 1: Save Your Meeting Recording
2. Save your meeting recording (can be .mp4, .mp3, etc.) in the `transcript` folder (this repo)
   - Use the file name `meeting.mp4` 

## Step 2: Point the script to the file (if needed)
Open `transcription_charlie.py` and change this line to match your file name:
```python
audio_file = "/Users/charlottelau/Documents/LTAIT/transcript/meeting.mp4"
```
Replace the path with the new path, if needed. This step can be skipped if you're running this in the same place each time. 

## Step 3: Run the Script
1. Open the script in Cursor
2. Click the Play button (▶️) in the top right corner

Note that this may take a while. To fetch a transcript for a 2-3 hour video, the script runtime is 5-10 minutes. 

## Step 4: Get Your Transcript
The transcript will appear in the same folder as your recording with "_transcription.txt" added to the name.
- If your recording was `meeting.mp4`, the transcript will be `meeting_transcription.txt`
The format will show as 
[HH:MM:SS - HH:MM:SS Transcription text]
... and it will show the new text for every few seconds, not when the speaker changes.

## First Time Setup (Only Need to Do Once)
Run these commands in the terminal:
```bash
pip install openai-whisper torch ffmpeg-python
brew install ffmpeg  # If you're on Mac
``` 

## Other Notes

### Speaker differentiation (or lack thereof)
We've tried, separately, to differentiate speakers, and all the attempts have failed. 
Therefore, this is the "dumbest" version of transcription model, which does Speech-to-Text transcription of all spoken words for every couple seconds, regardless of who is speaking. 

### Saving old transcripts
- If you're using the same file names, this script will overwrite any existing file with the same name (e.g. running a new version with "meeting" will mean this week's meeting_transcription.txt overwrite's last week's file). If you want to keep the previous version, copy it to a new location, or rename the old file before runniung the code again. 