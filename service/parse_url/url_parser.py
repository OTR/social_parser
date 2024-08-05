""""""
from urllib.parse import urlparse
import re


class UrlParser:
    """"""

    @staticmethod
    def get_platform(url: str) -> str:
        """"""
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split('.')

        if len(domain_parts) > 1:
            if domain_parts[-2] == "youtu":
                return "YOUTUBE"
            return domain_parts[-2].upper()
        raise ValueError("Domain should contain at least 2 parts")

    @staticmethod
    def get_content_id(url: str) -> str:
        """"""
        platform: str = UrlParser.get_platform(url)
        if platform == "X":
            return UrlParser._get_x_content_id(url)
        elif platform == "YOUTUBE":
            return UrlParser._get_youtube_content_id(url)
        elif platform == "INSTAGRAM":
            return UrlParser._get_instagram_content_id(url)
        elif platform == "TIKTOk":
            return UrlParser._get_tiktok_content_id(url)
        else:
            raise ValueError(f"Unknown platform {platform}")

    @staticmethod
    def _get_x_content_id(url: str) -> str:
        """"""
        pattern = r'https://x\.com/[a-zA-Z0-9_]+/status/(\d+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Could not find Twitter status ID from the given link " + url)

    @staticmethod
    def _get_youtube_content_id(url: str) -> str:
        """"""
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/shorts/([^/?&]+)',  # For shorts
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?.*v=([^/?&]+)',  # For watch
            r'(?:https?://)?youtube\.com/shorts/([^/?&]+)',  # For shorts without www
            r'(?:https?://)?youtu\.be/([^/?&]+)'  # For youtu.be
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        raise ValueError("Could not find Youtube video ID from the given link " + url)

    @staticmethod
    def _get_instagram_content_id(url: str) -> str:
        """"""
        pattern = r'https://www\.instagram\.com/(?:reel|p)/([A-Za-z0-9_-]+)/?'
        match = re.search(pattern, url)
        if match:
            return match.group(1)

        raise ValueError("Could not find Instagram post/reels ID from the given link " + url)

    @staticmethod
    def _get_tiktok_content_id(url: str) -> str:
        """"""
        pattern = re.compile(r'https?://www\.tiktok\.com/@[^/]+/video/(\d+)')
        match = pattern.search(url)
        if match:
            return match.group(1)

        raise ValueError("Could not find Tiktok video ID from the given link " + url)


if __name__ == "__main__":
    print(UrlParser.get_content_id("https://x.com/urrrswtht/status/1812872916519756282"))
    print(UrlParser.get_content_id("https://x.com/DantesDmitriy/status/1816143577036251642"))
    print(UrlParser.get_content_id("https://www.instagram.com/reel/C9r_0ruov32"))
    print(UrlParser.get_content_id("https://www.instagram.com/p/C94CTSZCvvn/"))
    print(UrlParser.get_content_id("https://www.youtube.com/shorts/tKFVgdnK2ks"))
    print(UrlParser.get_content_id("https://www.youtube.com/watch?v=SN2l4GPBQv8"))
    print(UrlParser.get_content_id("https://www.tiktok.com/@karolinakeleshian/video/7398067559024643346"))
    print(UrlParser.get_content_id("https://www.tiktok.com/@d.chert/video/7394912485314252040?_t=8oKFButr1GR&_r=1"))
    print(UrlParser.get_content_id("https://www.youtube.com/shorts/tKFVgdnK2ks"))
    print(UrlParser.get_content_id("https://www.youtube.com/watch?app=desktop&v=KK2EHRLuZvg"))
    print(UrlParser.get_content_id("https://youtube.com/shorts/dWIkGQt3xMw?si=poPoLKCfgdkXYm9G"))
    print(UrlParser.get_content_id("https://youtu.be/OCiaMzkim5A?si=BHa6D9WrgiR2Psdo"))
