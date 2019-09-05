class Counter(object):
  def __init__(self, low, heigh):
    self.current = low
    self.heigh = heigh

  def __iter__(self):
    'Returns itself as an iterator object'
    return self

  def __next__(self):
    'Returns the next value till current is lower than high'
    if self.current > self.heigh:
      raise StopIteration
    else:
      self.current += 1
      return self.current - 1
        

if __name__ == '__main__':
    print('Hello iterator')
