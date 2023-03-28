class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.__capacity = capacity
        self.__data = dict()

    def get(self, key: str) -> str:
        if key in self.__data:
            value = self.__data[key]
            del self.__data[key]
            self.__data[key] = value
            return value
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        if key in self.__data:
            del self.__data[key]
        elif len(self.__data) >= self.__capacity:
            del self.__data[next(iter(self.__data))]
        self.__data[key] = value

    def rem(self, key: str) -> None:
        if key in self.__data:
            del self.__data[key]
