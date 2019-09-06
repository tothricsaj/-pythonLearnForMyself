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
        

class GetAlphabet(object):
  def __init__(self, beginChar):
      """
      It will rais AttributeError if the attribute is not str and longer than 1'
      """
      if isinstance(beginChar, str) and len(beginChar) == 1:
          self.beginChar = beginChar
      else:
          raise AttributeError

  def __iter__(self):
    'Returns itself as an iterator object'
    print('Iterator is birthing.....\n')
    return self

  def __next__(self):
    'Returns the next value till current is lower than high'
    if ord(self.beginChar) >= 123:
      raise StopIteration
    else:
      self.beginChar = chr(ord(self.beginChar) + 1)
      return chr(ord(self.beginChar) - 1)



if __name__ == '__main__':
    print('Hello iterator\n')

    ga = GetAlphabet('g')

    for i in ga:
        print(i, end=" - ")
