""""""
from googleapiclient.discovery import build
from datetime import datetime


DEVELOPER_KEY = "AIzaSyCLBJESzFDNFYoOXkq40wgEdOXyTE_Us3g"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

COOKIE_CUTTERS = {
    "UCKeiw4bjGb80LuGhasWpwUA",  # Arsen Markaryan Errday
    "UC6hLw66ZPkEGJKgnWpbsX4w",  # Markaryan Tendency
    "UCx4msx5RPNoNymPnW8b9mqw",  # @narezus
    "UC4BYNwB6Z7sLqpr0DpJ2vxQ",  # Anton Guskov | podkast
    "UCQrubYUwYoDIVDRuHR7_wcQ",  # Deep Baza
    "UCby0W8sleMF3LI8uwbUA9uQ",  # ArserLife
    "UCQ2C4JrOuqfsX2X5gSsXlQw",  # МОТИВАТОРИКА
    "UCmmUh_zeDU4NTU2sKdi276w",  # PRO Бизнес
    "UCF_Z9gbuNQsdCWhUEJBAJKQ",  # Мудрая База
    "UCavkcYNJfaugPqSZAalX07g",  # МЫСЛЕТРЕНДЫ
    "UCzHfajgDRqqCkEADOgfqGfA",  # Markaryan_Base
    "UCTXaAPflcjldGp-rpDoKLWA",  # Growth Area
    "UCF_PIOGFK0JvfW-m1EncjqA",  # Арсен Маркарян Подкасты
    "UCElNqaiwqrW3TLaO-aTGBHw",  # Grind University Слив | Арсен Маркарян
    "UCEgxjr-XMxuG-qWIyIhv72A",  # Арсен Маркарян | Grind University
    "UCIHeLSqN5Cv0pFwBIWBBdtw",  # zanosik4
    "UCB-oSrxvaDi108__dCRCFUQ",  # only
    "UCnYfSIsNYgVM1iEH3_YGJAw",  # Арсенистан
    "UCy1k6iJN4QQDNn7bAjNN4QQ",  # Проект "Акула"
    "UCybnmBggf6D0ZsQk_VlGBgw",  # Джус podcast
    "UCfJn1Jcp1Krt51-DdzbpjrQ",  # Апгрейд
    "UC78PAEujTahZqkn83gSQFYw",  # Мастерская Интервью
    "UC4l22KH88KgnTdyrX9B_gdw",  # chumaboy_164
    "UCbHDZGmGCcLRZlRSUD_07Ww",  # Motivator Notes
    "UCEoSo_wtM1J_DoSSqJ3Bg7Q",  # Подкасты Арсена Маркаряна
    "UCU87aPPaMgNdKdXBJV1jmrg",  # Grzybky 228
    "UC-3bHLMDGBxsDI3xn6_OiCQ",  # Alone
    "UCcsyPkUmml9QEhom9wjnmTA",  # ShortCast
    "UCI8qIDTvIgpgS378N0IPMuA",  # Альфа Доступ к Базе
    "UC_w0Sv8tztL7fqxnoeDDKfQ",  # Арсен Маркарян Официальный Shorts
    "UC7G1JJmAc-zGicaMOgAquXA",  # Арсен Маркарян
    "UC9scATp5FnEnouNqcRyYHoA",  # Бригада Арсена Маркаряна
    "UCFfDebQoDURriy32Fg7ZvKg",  # LoveShorts
    "UCiAbSBhhG61ZxNtJHDS0-_A",  # Артем
    "UCMzntpQgC3M-TnflqXxNkGA",  # MOTIVATIONSARSENA
}

REJECTED = ""


def youtube_search_keyword(query, max_results, page_token=None):
    youtube_object = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )
    search_keyword = youtube_object.search().list(
        q=query,
        order="date",
        type="video",
        safeSearch="none",
        videoDuration="any",
        regionCode="RU",
        part="id, snippet",
        maxResults=max_results,
        pageToken=page_token
    ).execute()

    next_page_token = search_keyword.get("nextPageToken")
    results = search_keyword.get("items", [])

    print(next_page_token)
    for result in results:
        title: str = result["snippet"]["title"]
        published_at: str = result["snippet"]["publishedAt"]
        published_datetime = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
        channel_title: str  =result["snippet"]["channelTitle"]
        channel_id: str = result["snippet"]["channelId"]
        video_id: str = result["id"]["videoId"]
        description: str = result['snippet']['description']
        thumbnail_url: str = result['snippet']['thumbnails']['default']['url']
        if channel_id not in COOKIE_CUTTERS:
            print(f" {channel_id} {channel_title} {video_id} {title}")


if __name__ == "__main__":
    youtube_search_keyword(
        'маркарян',
        max_results=50,
        #page_token="CDIQAA"
    )
