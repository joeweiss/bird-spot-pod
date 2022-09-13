import os
from ebird.api import get_nearby_observations
from pprint import pprint
from pydub import AudioSegment
from os.path import join
from gtts import gTTS
from io import BytesIO

EBIRD_API_KEY = os.environ.get("EBIRD_API_KEY", "")
LON = os.environ.get("LONGITUDE", "")
LAT = os.environ.get("LATITUDE", "")

AUDIO_DIRECTORY = (
    "/usr/audio/The Cornell Guide to Bird Sounds--United States and Canada (v2021)/"
)

NUM_OF_BIRDS_TO_INCLUDE = 5


def run():
    print("sing")
    records = get_nearby_observations(EBIRD_API_KEY, LAT, LON, dist=15, back=7)
    pprint(records)
    common_names = list(set([i["comName"] for i in records]))[0:NUM_OF_BIRDS_TO_INCLUDE]
    # Find recordings starting with the common name ...
    filenames = os.listdir(AUDIO_DIRECTORY)

    print(common_names)
    outputSegments = None
    for name in common_names:
        # Find filenames
        print("-" * 80)
        print(name)
        recordings = [i for i in filenames if i.startswith(name)]
        print(recordings)

        filepath = join(AUDIO_DIRECTORY, recordings[0])
        song = AudioSegment.from_mp3(filepath)
        if outputSegments:
            song = AudioSegment.from_mp3(filepath)
            outputSegments = outputSegments.append(song, crossfade=2000)
        else:
            outputSegments = AudioSegment.from_mp3(filepath)

        # Add notation.
        mp3_fp = BytesIO()
        tts = gTTS(f"That was a {name}", lang="en")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        narration = AudioSegment.from_mp3(mp3_fp)
        outputSegments = outputSegments.append(narration, crossfade=500)
        outputSegments = outputSegments.append(AudioSegment.silent(duration=2000))

    outputSegments.export("output.mp3", format="mp3")
