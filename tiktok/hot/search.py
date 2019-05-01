from tiktok.structures import HotSearch
from tiktok.utils import fetch


def search(hot_search_url, **kwargs):
    """
    get hot search result
    :return: HotSearch object
    """
    result = fetch(hot_search_url, **kwargs)
    # process json data
    datetime = result.get('data', {}).get('active_time')
    word_list = result.get('data', {}).get('word_list', [])
    data = [{'item': item.get('word'), 'hot_value': item.get('hot_value')} for item in word_list]
    # construct HotSearch object and return
    return HotSearch(datetime=datetime, data=data)
