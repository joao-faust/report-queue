from typing import Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
  def __init__(self, values: list[T] = []):
    self.__values = values

  def enqueue(self, value: T):
    self.__values.append(value)

  def dequeue(self):
    self.__values.pop(0)

  def has_values(self):
    return True if len(self.__values) > 0 else False

  def get_values(self):
    return self.__values

  def get_value(self, posi: int):
    for i, value in enumerate(self.__values):
      if i == posi:
        return value
    return None

  def get_first(self):
    return self.get_value(0)

  def clear(self):
    self.__values.clear()
