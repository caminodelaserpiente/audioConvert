import os


import whisper
import moviepy.editor


def model_whisper():
    try:
        model = whisper.load_model("small")
        return model
    except:
        print("[Error] To load whisper.\n")
        return None


def get_path_mp3():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = input("\nEnter path file .mp3.\n>>> ")
            if not response.endswith(".mp3"):
                raise ValueError("[Error] Please enter a valid path (.mp3).\n")
            return response
        except ValueError:
            attempts += 1
            print("[Error] Please enter a valid path (.mp3).\n")


def get_path_mp4():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = input("\nEnter path file .mp4.\n>>> ")
            if not response.endswith(".mp4"):
                raise ValueError("[Error] Please enter a valid path (.mp4).\n")
            return response
        except ValueError:
            attempts += 1
            print("[Error] Please enter a valid path (.mp4).\n")


def audio_convert(response, model, path_mp3):
    if response == 1:
        _transcription_to_text(model, path_mp3)
    elif response == 2:
        _transcription_to_subtitle(model, path_mp3)
    else:
        print("[Error] Please enter a valid option.")


def video_to_audio(path_video):
    try:
        # Create output folfer
        output_folder = './output/mp3/'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        # Extract name file
        name_file = os.path.splitext(os.path.basename(path_video))[0]
        audio_name = os.path.join(output_folder, name_file + ".mp3")
        # Extract audio from .mp4
        print(f"\n[OK 1/2] Extracting audio from video...")
        video = moviepy.editor.VideoFileClip(path_video)
        audio = video.audio
        audio.write_audiofile(audio_name)
        print(f"\n[OK 2/2] Extracting audio from video successful.")
        return audio_name
    except KeyError:
        print('[ERROR] Video not supported. Try another')
    except OSError:
        print(f"[ERROR] The file '{path_video}'could not be found")
    except Exception:
        print('[Error] No correct path entered')


def _transcription_to_text(model, path):
    try:
        # Create output folfer
        output_folder = './output/texts'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        # Extract name file
        name_file = os.path.splitext(os.path.basename(path))[0]
        output_path = f'{output_folder}/{name_file}.txt'
        # Extract text from .mp3
        print(f"\n[OK 1/2] Converting audio to text...")
        result = model.transcribe(path)
        with open(output_path, "w", encoding="utf-8") as f:
            for row in result['segments']:
                text = row['text']
                f.writelines(text)
                f.writelines("\n")
        print(f"[OK 2/2] Your file has been created: {output_path}")
    except TypeError:
        print('[Error] No correct path entered')
    except Exception:
        print('[Error] No correct path entered')


def _transcription_to_subtitle(model, path):
    try:
        # Create output folfer
        output_folder = './output/subtitles'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        # Extract name file
        name_file = os.path.splitext(os.path.basename(path))[0]
        output_path = f'{output_folder}/{name_file}.sbv'
        # Extract text from .mp3
        print(f"\n[OK 1/2] Converting audio to subtitles...")
        result = model.transcribe(path)
        with open(output_path, "w", encoding="utf-8") as f:
            for row in result['segments']:
                start = _format_time(int(row['start']))
                end = _format_time(int(row['end']))
                text = row['text']
                time = start + "," + end
                lyric = text
                f.writelines(time)
                f.writelines("\n")
                f.writelines(lyric)
                f.writelines("\n\n")
        print(f"[OK 2/2] Your file has been created: {output_path}")
    except Exception:
        print('[Error] No correct path entered')


def _format_time(seconds):
    hours = int(seconds / 60 / 60)
    seconds -= hours*60*60
    minutes = int(seconds/60)
    seconds -= minutes*60
    milliseconds = ".000"
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}{milliseconds}"
