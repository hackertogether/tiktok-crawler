from tiktok.structures import *
from tiktok.utils.common import first, parse_datetime


def data_to_video(data):
    """
    transfer json data to video object
    :param data:
    :return:
    """
    statistics = data.get('statistics', {})
    like_count = statistics.get('digg_count')
    comment_count = statistics.get('comment_count')
    share_count = statistics.get('share_count')
    id = statistics.get('aweme_id')
    desc = data.get('desc')
    is_ads = data.get('is_ads')
    duration = data.get('duration')
    create_time = parse_datetime(data.get('create_time'))
    share_url = data.get('share_url')
    ratio = data.get('video', {}).get('ratio')
    cover_url = first(data.get('video', {}).get('origin_cover', {}).get('url_list'))
    play_url = data.get('video', {}).get('play_addr', {}).get('url_list')[-1]
    author = data_to_user(data.get('author', {}))
    music = data_to_music(data.get('music', {}))
    address = data_to_address(data.get('poi_info', {}))
    return Video(
        id=id,
        desc=desc,
        like_count=like_count,
        share_count=share_count,
        comment_count=comment_count,
        is_ads=is_ads,
        duration=duration,
        create_time=create_time,
        share_url=share_url,
        ratio=ratio,
        cover_url=cover_url,
        play_url=play_url,
        author=author,
        music=music,
        address=address
    ) if id else None


def data_to_music(data):
    """
    transfer data to music object
    :param data:
    :return:
    """
    id = data.get('mid')
    name = data.get('title')
    play_url = data.get('play_url', {}).get('url_list', [])[-1]
    owner_id = data.get('owner_id')
    owner_name = data.get('owner_nickname')
    cover_url = first(data.get('cover_large', {}).get('url_list', []))
    return Music(
        id=id,
        name=name,
        play_url=play_url,
        owner_id=owner_id,
        owner_name=owner_name,
        cover_url=cover_url
    ) if id else None


def data_to_user(data):
    """
    transfer data to user object
    :param data:
    :return:
    """
    alias = data.get('unique_id') or data.get('short_id')
    _id = data.get('uid')
    name = data.get('nickname')
    sign = data.get('signature')
    avatar = first(data.get('avatar_larger', {}).get('url_list', []))
    gender = data.get('gender')
    birthday = data.get('birthday')
    create_time = parse_datetime(data.get('create_time'))
    verify = bool(data.get('custom_verify').strip())
    verify_info = data.get('custom_verify').strip()
    return User(
        id=_id,
        alias=alias,
        name=name,
        sign=sign,
        avatar=avatar,
        gender=gender,
        verify=verify,
        verify_info=verify_info,
        create_time=create_time,
        birthday=birthday
    ) if _id else None


def data_to_address(data):
    """
    transfer data to address object
    :param data:
    :return:
    """
    _id = data.get('poi_id')
    address_info = data.get('address_info', {})
    province = address_info.get('province')
    city = address_info.get('city')
    district = address_info.get('district')
    full = address_info.get('simple_addr')
    address = address_info.get('address')
    postal_code = data.get('type_code')
    longitude = data.get('longitude')
    latitude = data.get('latitude')
    place = data.get('poi_name')
    return Address(
        id=_id,
        province=province,
        city=city,
        district=district,
        address=address,
        full=full,
        postal_code=postal_code,
        longitude=longitude,
        latitude=latitude,
        place=place
    ) if _id else None


def data_to_topic(data):
    """
    transfer data to topic object
    :param data:
    :return:
    """
    _id = data.get('cid')
    view_count = data.get('view_count')
    user_count = data.get('user_count')
    name = data.get('cha_name')
    desc = data.get('desc')
    return Topic(
        id=_id,
        view_count=view_count,
        user_count=user_count,
        name=name,
        desc=desc
    ) if _id else None
