from abc import ABC, abstractmethod

class Report(ABC):
  def __init__(self, name: str):
    self._name = name

  def get_name(self):
    return self._name

  @abstractmethod
  def generate(self, filename: str):
    pass
