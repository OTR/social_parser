""""""
import json
from pathlib import Path
from typing import IO

import requests


def download():
    """
    Calls remote RapidAPI service to gather recently uploaded videos by the given keyword
    """
    url = "https://tokapi-mobile-version.p.rapidapi.com/v1/search/post"
    querystring = {
        "keyword": "Арсен Маркарян",
        "count": "10",
        "offset": "0",
        "sort_type": "3"
    }
    headers = {
        "x-rapidapi-key": "720c100c23msh8c84982e4e4bedap1b37c6jsnb1496b6f5e23",
        "x-rapidapi-host": "tokapi-mobile-version.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def read_from_tokapi_mobile():
    """
    Reads JSON file from filesystem to not waste API call quotas
    Prints out author, description and url of found videos
    """
    parent_path: Path = Path(".").absolute().parent.parent
    path_to_json_sample: Path = (parent_path
                                 / ".data"
                                 / "tokapi_mobile_response_sample.json").resolve()
    file: IO[str] = open(path_to_json_sample)
    json_s = json.load(file)
    items = json_s["search_item_list"]
    for item in items:
        author: str = item["aweme_info"]["author"]["nickname"]
        description: str = item["aweme_info"]["desc"]
        url: str = item["aweme_info"]["share_info"]["share_url"]
        print(author)
        print(description)
        print(url)
        print("_" * 80)


if __name__ == '__main__':
    # download()
    read_from_tokapi_mobile()
