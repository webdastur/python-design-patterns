from abc import ABC


class MediaPlayer(ABC):
    def play(self, audio_type: str, file_name: str):
        pass


class AdvancedMediaPlayer(ABC):
    def play_vlc(self, file_name: str):
        pass

    def play_mp4(self, file_name: str):
        pass


class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str):
        print(f"Playing vlc file. Name: {file_name}")


class Mp4Player(AdvancedMediaPlayer):
    def play_mp4(self, file_name: str):
        print(f"Playing mp4 file. Name: {file_name}")


class MediaAdapter(MediaPlayer):
    advanced_music_player: AdvancedMediaPlayer

    def __init__(self, audio_type: str):
        if audio_type.lower() == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_music_player = Mp4Player()
        else:
            raise Exception(f"{audio_type} is not supported.")

    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "vlc":
            self.advanced_music_player.play_vlc(file_name)
        elif audio_type.lower() == "mp4":
            self.advanced_music_player.play_mp4(file_name)
        else:
            raise Exception(f"{audio_type} is not supported.")


class AudioPlayer(MediaPlayer):
    media_adapter: MediaAdapter

    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp3":
            print(f"Playing mp3 file. Name: {file_name}")
        elif audio_type.lower() == "vlc" or audio_type.lower() == "mp4":
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)
        else:
            print(f"Invalid media. {audio_type} format not supported")


if __name__ == "__main__":
    audio_player: AudioPlayer = AudioPlayer()

    audio_player.play("mp3", "beyond the horizon.mp3")
    audio_player.play("mp4", "alone.mp4")
    audio_player.play("vlc", "far far away.vlc")
    audio_player.play("avi", "mind me.avi")
