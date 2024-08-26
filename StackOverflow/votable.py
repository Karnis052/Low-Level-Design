from abc import ABC, abstractmethod

class Votable(ABC):
    @abstractmethod
    def vote(self, user, value):
        pass
    @abstractmethod
    def getVoteCount(self):
        pass