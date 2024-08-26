from abc import ABC, abstractmethod
class Commentable(ABC):
    @abstractmethod
    def addComment(self, comment):
        pass
    @abstractmethod
    def getComments(self):
        pass