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
    base_dir = "/Users/rupal/Documents/GitHub/Ego4d/dataset/takes/indiana_music_14_3"
    video_names = ["aria01_214-1.mp4", "cam01.mp4", "cam02.mp4", "cam03.mp4", "cam04.mp4"]

    for video_name in video_names:
        video_path = os.path.join(base_dir, "frame_aligned_videos", video_name)
        output_folder = os.path.join(base_dir, "frames_from_videos", video_name.split(".")[0])

        extract_frames(video_path, output_folder)


        print("reading from ", video_path)
        print("writing to", output_folder)