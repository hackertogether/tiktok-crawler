import tiktok
from tiktok.config import hot_trend_url, common_headers, common_parameter
from tiktok.structures import Topic, Music

# define handler
db_handler = tiktok.handlers.DBHandler()
file_handler = tiktok.handlers.FileHandler(folder='./videos')

# define downloader and specify handler
downloader = tiktok.downloaders.VideoDownloader([file_handler])

for result in tiktok.hot.trend(hot_trend_url, count=1, headers=common_headers):
    for item in result.data:
        # download videos of topic/music for 100 max per
        if isinstance(item, Topic):
            print('Get topic', item)
            downloader.download(item.videos(max=1), headers=common_headers, params=common_parameter)
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=1), headers=common_headers, params=common_parameter)
