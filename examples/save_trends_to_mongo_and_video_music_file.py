import tiktok
from tiktok.structures import Topic, Music

# define file handler and specify folder
video_file_handler = tiktok.handlers.VideoFileHandler(folder='./videos')
music_file_handler = tiktok.handlers.MusicFileHandler(folder='./musics')
# define db handler
db_handler = tiktok.handlers.DBHandler(conn_uri='localhost')
# define downloader
downloader = tiktok.downloaders.VideoDownloader([db_handler, video_file_handler, music_file_handler])

for result in tiktok.hot.trend():
    for item in result.data:
        # download videos of topic/music for 30 max per
        if isinstance(item, Topic):
            print('Item', item)
            downloader.download(item.videos(max=30))
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=30))
