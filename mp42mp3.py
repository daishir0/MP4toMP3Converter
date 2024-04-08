import sys
import subprocess

def convert_mp4_to_mp3(mp4_file_path):
    # 出力ファイル名を.mp4から.mp3に変更
    mp3_file_path = mp4_file_path.rsplit('.', 1)[0] + '.mp3'

    # ffmpegコマンドを使って変換
    ffmpeg_path = 'C:\\ffmpeg\\bin\\ffmpeg.exe'  # ffmpegのパスを適宜変更
    command = [ffmpeg_path, '-i', mp4_file_path, '-vn', '-ab', '128k', '-ar', '44100', '-y', mp3_file_path]
    subprocess.run(command)

    print(f'{mp4_file_path} を {mp3_file_path} に変換しました。')

if __name__ == '__main__':
    # コマンドライン引数からMP4ファイルのパスを取得
    if len(sys.argv) < 2:
        print("使用法: python mp42mp3.py <mp4ファイルのパス>")
        sys.exit(1)

    mp4_file_path = sys.argv[1]
    convert_mp4_to_mp3(mp4_file_path)
