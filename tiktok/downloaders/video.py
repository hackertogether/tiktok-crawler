from tiktok.structures import Video
from tiktok.handlers import Handler
from tiktok.downloaders import Downloader


class VideoDownloader(Downloader):
    
    async def process_item(self, obj, **kwargs):
        """
        process item
        :param obj: single obj
        :return:
        """
        if isinstance(obj, Video):
            print('Processing', obj, '...')
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    await handler.process(obj, **kwargs)
