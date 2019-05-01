import tiktok
from tiktok.structures import Topic, Music
from tiktok.config import hot_trend_url, common_headers, common_parameter

# define file handler and specify folder
file_handler = tiktok.handlers.FileHandler(folder='./videos')
# define db handler
db_handler = tiktok.handlers.DBHandler()
# define downloader
downloader = tiktok.downloaders.VideoDownloader([file_handler, db_handler])

for result in tiktok.hot.trend(hot_trend_url, count=1, headers=common_headers):
    for item in result.data:
        # download videos of topic/music for 200 max per
        if isinstance(item, Topic):
            print('Item', item)
            downloader.download(item.videos(max=30), headers=common_parameter, params=common_parameter)
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=30), headers=common_parameter, params=common_parameter)
