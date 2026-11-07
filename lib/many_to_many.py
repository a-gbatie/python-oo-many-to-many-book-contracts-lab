class Author:
    pass


class Book:
  all = [] # list to store all books
  
  def __init__(self, title):
    self.title = title
    Book.all.append(self)
  
  def contracts(self):
    return [
      contract for contract in Contract.all # list comprehension to filter contracts for book
      if contract.book == self
    ]

  def authors(self):
    return list(set(contract.author for contract in self.contracts())) # finds all authors for particular book

class Contract:
    pass