from abc import abstractmethod


class AbstractBot:
    @abstractmethod
    def run(self):
        ...
