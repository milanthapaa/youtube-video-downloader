from pytube import Playlist


def download_yt_playlist():
    playlist = Playlist("https://www.youtube.com/playlist?list=PLrzb5ti9EMxb43gxMUI1U9epbSO2pyLPg")
    print(f"Downloading: {playlist.title}")
    for video in playlist.videos:
        video.streams.first().download()


if __name__ == '__main__':
    download_yt_playlist()
