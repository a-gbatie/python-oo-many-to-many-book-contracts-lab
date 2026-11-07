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
  
  def sign_contracts(self, book, date, royalties):
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
    pass