from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from ..Queue import Queue

T = TypeVar('T')

class Menu(Generic[T], ABC):
  def __init__(self, queue: Queue[T]):
    self._queue = queue

  @abstractmethod
  def show_options(self):
    pass

  @abstractmethod
  def add_item(self):
    pass

  @abstractmethod
  def display_items(self):
    pass

  def get_methods(self):
    return {
      '1': self.add_item,
      '2': self.display_items,
    }
