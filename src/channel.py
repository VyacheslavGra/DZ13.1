import json
import os
from googleapiclient.discovery import build

'''Клонировал проект'''

import isodate


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.description: str = self.__channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriber_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.name = self.__channel['items'][0]['snippet']['title']
        self.view_count = int(self.__channel['items'][0]['statistics']['viewCount'])
        self.title = self.__channel["items"][0]["snippet"]["title"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.__channel)

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    @classmethod
    def get_service(cls) -> str:
        return cls.youtube

    def to_json(self, json_file: str) -> None:
        """Записывает данные канала в указанный аргументом json file"""
        with open(json_file, 'w', encoding='utf8') as f:
            json.dump(self.__channel, f, indent=2, ensure_ascii=False)

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
