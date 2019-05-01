import tiktok

# HotVideo
from tiktok.config import hot_video_url, common_headers, common_parameter, hot_music_url

# HotMusic
result = tiktok.hot.music(hot_music_url, headers=common_headers, params=common_parameter)
# music objects
musics = result.data
# print every music
for music in musics:
    print(music)

# define handler and specify folder
handler = tiktok.handlers.FileHandler(folder='./musics')
# define downloader
downloader = tiktok.downloaders.MusicDownloader([handler])
# download musics
downloader.download(musics, headers=common_headers, params=common_parameter)

result = tiktok.hot.video(hot_video_url, headers=common_headers, params=common_parameter)
# video objects
videos = result.data
# print every video
for video in videos:
    print(video)

# define handler and specify folder
handler = tiktok.handlers.FileHandler(folder='./videos')
# define downloader
downloader = tiktok.downloaders.VideoDownloader([handler])
# download videos
downloader.download(videos, headers=common_headers, params=common_parameter)
