from tiktok.structures import Music
from tiktok.handlers import Handler
from tiktok.downloaders import Downloader


class MusicDownloader(Downloader):
    
    async def process_item(self, obj, **kwargs):
        """
        process item
        :param obj: single obj
        :return:
        """
        if isinstance(obj, Music):
            print('Processing', obj, '...')
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    await handler.process(obj, **kwargs)
