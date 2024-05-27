import os
import subprocess

def extract_frames(video_path, output_folder, fps=1):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construct the ffmpeg command
    output_pattern = os.path.join(output_folder, 'frame_%04d.png')
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'fps={fps}',
        output_pattern
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"Frames extracted successfully to {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while extracting frames: {e}")

if __name__ == "__main__":
    # Example usage
    video_path = "/Users/rupal/Documents/GitHub/Ego4d/dataset/takes/nus_cpr_06_2/frame_aligned_videos/aria01_214-1.mp4"
    output_folder = "/Users/rupal/Documents/GitHub/Ego4d/dataset/takes/nus_cpr_06_2/frames_from_videos/aria01_214-1"

    extract_frames(video_path, output_folder)
