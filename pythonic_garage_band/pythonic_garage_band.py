from abc import ABC, abstractmethod


class Band:
    band_list = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.band_list.append(self)

    def play_solos(self):
        solos = []
        return [member.play_solo() for member in self.members]

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def to_list(cls):
        return cls.band_list


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
