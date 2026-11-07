class Author:
  all = [] # list to store all authors
  
  def __init__(self, name):
    self.name = name
    Author.all.append(self)
    
  def contracts(self):
    return [
      contract for contract in Contract.all # list comprehension to filter contracts for author
      if contract.author == self
    ]
  
  def books(self):
    return list(set(contract.book for contract in self.contracts())) # finds all books for particular author
  
  def sign_contract(self, book, date, royalties):
    return Contract(self, book, date, royalties)
  
  def total_royalties(self):
    return sum(contract.royalties for contract in self.contracts()) # calculates total royalties for author


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
  all = [] # list to store all contracts
  
  def __init__(self, author, book, date, royalties):
    self.author = author
    self.book = book
    self.date = date
    self.royalties = royalties
    Contract.all.append(self)
  
  @property
  def author(self):
    return self._author
  
  @author.setter
  def author(self, value):
    if not isinstance(value, Author):
      raise ValueError("Author must be an Author object")
    self._author = value

  @property
  def book(self):
    return self._book
  
  @book.setter
  def book(self, value):
    if not isinstance(value, Book):
      raise ValueError("Book must be a Book object")
    self._book = value
    
  @property
  def date(self):
    return self._date
  
  @date.setter
  def date(self, value):
    if not isinstance(value, str):
      raise ValueError("Date must be a string")
    self._date = value

  @property
  def royalties(self):
    return self._royalties
  
  @royalties.setter
  def royalties(self, value):
    if not isinstance(value, int):
      raise ValueError("Royalties must be an integer")
    self._royalties = value
    
  @classmethod
  def contracts_by_date(cls, date):
    return [
      contract for contract in cls.all
      if contract.date == date
    ]
  