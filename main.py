class Camera:
    def __init__(self, megapixels: int):
        self.megapixels = megapixels  # ексклюзивний атрибут Camera

    def take_photo(self) -> str:      #  метод Camera
        return f"Фото зроблено: {self.megapixels} Мп"


class GPS:
    def __init__(self, has_maps: bool):
        self.has_maps = has_maps      # ексклюзивний атрибут GPS

    def get_location(self) -> str:    #  метод GPS
        return "Локація: 47.84, 35.14"  #  координат


class MusicPlayer:
    def __init__(self, volume: int):
        self.volume = volume          # ексклюзивний атрибут MusicPlayer

    def play_music(self, song: str) -> str:  # метод MusicPlayer
        return f"Грає: {song} (гучність {self.volume})"


class Smartphone(Camera, GPS, MusicPlayer):
    def __init__(self, model: str, megapixels: int, has_maps: bool, volume: int):
        self.model = model
        Camera.__init__(self, megapixels)
        GPS.__init__(self, has_maps)
        MusicPlayer.__init__(self, volume)

    def info(self) -> str:
        return f"Смартфон {self.model}: камера {self.megapixels}Мп, maps={self.has_maps}, volume={self.volume}"


# Перевірка
phone = Smartphone("Pixel", megapixels=50, has_maps=True, volume=7)

print(phone.info())
print(phone.take_photo())
print(phone.get_location())
print(phone.play_music("Song A"))