import soundfile as sf
import sounddevice as sd


class Player():
    """Player for .it files
    """
    filename = None

    def __init__(self, filename=None):
        self.filename = filename

    def play(self):
        print('play: {}'.format(self.filename))
