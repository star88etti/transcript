# Video Concatenation Script

This script combines two videos into one, placing them back-to-back in the order you specify.

## Setup

1. Install the required package:
```bash
pip install moviepy
```

## Usage

1. Place your video files in the `transcript` folder
2. Open `concat_videos.py` in Cursor
3. Update these lines with your actual video file names:
```python
video1 = "/Users/charlottelau/Documents/LTAIT/transcript/video1.mp4"  # First video (1.5 hours)
video2 = "/Users/charlottelau/Documents/LTAIT/transcript/video2.mp4"  # Second video (45 minutes)
output = "/Users/charlottelau/Documents/LTAIT/transcript/combined_video.mp4"  # Output file
```

4. Run the script by clicking the Play button (▶️) in Cursor

## What to Expect

- The script will show you the duration of each video
- It will combine them in the order specified
- The final video will be saved as `combined_video.mp4` (or whatever name you specify)
- The process might take a while depending on the video lengths

## Troubleshooting

If you get an error:
1. Make sure both video files exist in the specified location
2. Check that you have enough disk space for the combined video
3. Ensure both videos are in a compatible format (MP4 is recommended) 