import collections
from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService


def test_list_book_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ['aaa-001', 'aaa-002']


def test_list_authors(monkeypatch):
       
    def mock_get_books(*args):
        return [
        {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        {'id': 'aaa-002', 'name': 'le jour', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        {'id': 'aaa-003', 'name': 'Anges & Démons', 'author': {'firstname': 'Danny', 'lastname': 'Boy'}},
    ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)
    book_service = BookService(book_fetcher_service=BookFetcherService())
    nom_prenom = book_service.list_books_authors()
    #['author']['lastname'] + ' ' + book['author']['firstname']
    # le resultat d assert est de comparer 2 tableau ordonés: collections.Counter
    assert collections.Counter(nom_prenom) == collections.Counter (['Brown Dan', 'Boy Danny'])
    
##################

def test_missing_authors_name(monkeypatch):
       
    def mock_get_books(*args):
        return [
        {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        {'id': 'aaa-002', 'name': 'le jour', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        {'id': 'aaa-003', 'name': 'Anges & Démons', 'author': {'firstname': '', 'lastname': ''}},
    ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)
    book_service = BookService(book_fetcher_service=BookFetcherService())
    nom_prenom = book_service.list_books_authors()
    #['author']['lastname'] + ' ' + book['author']['firstname']
    # le resultat d assert est de comparer 2 tableau non ordonés: collections.Counter
    assert collections.Counter(nom_prenom) == collections.Counter (['Brown Dan', ' '])


##################

def test_missing_author_firstname(monkeypatch):
       
    def mock_get_books(*args):
        return [
        {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        {'id': 'aaa-002', 'name': 'le jour', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        {'id': 'aaa-003', 'name': 'Anges & Démons', 'author': {'firstname': '', 'lastname': 'Malabata'}},
        {'id': 'aaa-004', 'name': 'le suivant', 'author': {'firstname': 'Maurice', 'lastname': 'becker'}},

    ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)
    book_service = BookService(book_fetcher_service=BookFetcherService())
    nom_prenoms = book_service.list_books_authors()

    assert collections.Counter(nom_prenoms) == collections.Counter(['Brown Dan','becker Maurice','Malabata '''])
   