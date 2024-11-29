from ffmpeg import FFmpeg
import os

input_file = 'Undead Man Walkin.mp3'
output_dir = 'Undead Man Walkin'
os.makedirs(output_dir, exist_ok=True)

segment_duration = 10
bitrates = [256, 128, 32]

for bitrate in bitrates:
    output_dir_bitrate = f"{output_dir} {str(bitrate)}kbps"
    os.makedirs(output_dir_bitrate, exist_ok=True)
    playlist = f"{output_dir} {str(bitrate)}k.m3u8"
    input_file_bitrate = input_file[:-4] + " " + str(bitrate) + "k.mp3"

    FFmpeg().input(input_file).output(
        os.path.join(output_dir, input_file_bitrate),
        {"b:a": str(bitrate) + "k"},
        acodec='libmp3lame'
    ).execute()

    FFmpeg().input(os.path.join(output_dir, input_file_bitrate)).output(
        os.path.join(output_dir_bitrate, 'output%03d.ts'),
        f='segment',
        segment_time=segment_duration,
        segment_list=playlist,
        reset_timestamps=1,
        c='copy',
    ).execute()
