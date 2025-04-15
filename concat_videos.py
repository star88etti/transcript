from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import traceback

class VideoConcatenator:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Concatenator")
        self.root.geometry("600x300")
        
        # Variables to store file paths
        self.video1_path = tk.StringVar()
        self.video2_path = tk.StringVar()
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Video 1 selection
        frame1 = tk.Frame(self.root)
        frame1.pack(fill=tk.X, padx=20, pady=10)
        
        label1 = tk.Label(frame1, text="First Video:")
        label1.pack(side=tk.LEFT)
        
        entry1 = tk.Entry(frame1, textvariable=self.video1_path, width=40)
        entry1.pack(side=tk.LEFT, padx=5)
        
        button1 = tk.Button(frame1, text="Browse", command=self.browse_video1, width=10)
        button1.pack(side=tk.LEFT)
        
        # Video 2 selection
        frame2 = tk.Frame(self.root)
        frame2.pack(fill=tk.X, padx=20, pady=10)
        
        label2 = tk.Label(frame2, text="Second Video:")
        label2.pack(side=tk.LEFT)
        
        entry2 = tk.Entry(frame2, textvariable=self.video2_path, width=40)
        entry2.pack(side=tk.LEFT, padx=5)
        
        button2 = tk.Button(frame2, text="Browse", command=self.browse_video2, width=10)
        button2.pack(side=tk.LEFT)
        
        # Concatenate button
        concat_button = tk.Button(self.root, text="Concatenate Videos", command=self.concatenate_videos, width=20)
        concat_button.pack(pady=20)
        
    def browse_video1(self):
        filename = filedialog.askopenfilename(
            title="Select First Video",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
        )
        if filename:
            self.video1_path.set(filename)
    
    def browse_video2(self):
        filename = filedialog.askopenfilename(
            title="Select Second Video",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
        )
        if filename:
            self.video2_path.set(filename)
    
    def concatenate_videos(self):
        video1 = self.video1_path.get()
        video2 = self.video2_path.get()
        
        if not all([video1, video2]):
            messagebox.showerror("Error", "Please select both videos!")
            return
        
        try:
            # Check if input files exist
            if not os.path.exists(video1):
                messagebox.showerror("Error", f"First video not found at: {video1}")
                return
            if not os.path.exists(video2):
                messagebox.showerror("Error", f"Second video not found at: {video2}")
                return
            
            # Get the directory of the first video for output
            output_dir = os.path.dirname(video1)
            # Create output filename based on input filenames
            video1_name = os.path.splitext(os.path.basename(video1))[0]
            video2_name = os.path.splitext(os.path.basename(video2))[0]
            output = os.path.join(output_dir, f"{video1_name}_{video2_name}_combined.mp4")
            
            # Create progress window
            progress = tk.Toplevel(self.root)
            progress.title("Processing...")
            progress.geometry("400x150")
            
            # Add progress label
            progress_label = tk.Label(progress, text="Starting video processing...")
            progress_label.pack(pady=10)
            
            # Add status label
            status_label = tk.Label(progress, text="")
            status_label.pack(pady=5)
            
            progress.update()
            
            try:
                # Update status
                status_label.config(text="Loading first video...")
                progress.update()
                print("Loading first video...")  # Debug print
                clip1 = VideoFileClip(video1)
                print(f"First video loaded. Duration: {clip1.duration} seconds")  # Debug print
                
                status_label.config(text="Loading second video...")
                progress.update()
                print("Loading second video...")  # Debug print
                clip2 = VideoFileClip(video2)
                print(f"Second video loaded. Duration: {clip2.duration} seconds")  # Debug print
                
                status_label.config(text="Combining videos...")
                progress.update()
                print("Combining videos...")  # Debug print
                final_clip = concatenate_videoclips([clip1, clip2])
                print("Videos combined successfully")  # Debug print
                
                status_label.config(text="Saving combined video...\nThis may take several minutes.")
                progress.update()
                print("Saving combined video...")  # Debug print
                
                # Write the result to a file
                final_clip.write_videofile(output)
                print(f"Video saved to: {output}")  # Debug print
                
                # Close the clips
                clip1.close()
                clip2.close()
                final_clip.close()
                
                progress.destroy()
                messagebox.showinfo("Success", f"Successfully created concatenated video!\nSaved to: {output}")
                
            except Exception as e:
                print(f"Error during processing: {str(e)}")  # Debug print
                print(traceback.format_exc())  # Debug print
                raise  # Re-raise the exception to be caught by the outer try block
            
        except Exception as e:
            error_msg = f"Error during video processing:\n{str(e)}\n\n{traceback.format_exc()}"
            messagebox.showerror("Error", error_msg)
            if 'progress' in locals():
                progress.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConcatenator(root)
    root.mainloop() 