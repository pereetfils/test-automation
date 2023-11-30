
from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService



def test_list_users(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {"id" : "001","email" : "khatira@sondomaine.fr"},
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
   
    user = user_service.list_users()

    assert user == [{'id': '001', 'email': 'khatira@sondomaine.fr'}]

###test de la case dans l email ###
def test_case_in_email_users(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {"id" : "001","email" : "khatirA@sondomaine.fr"},
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
   
    user = user_service.list_users()

    assert user == [{'id': '001', 'email': 'khatira@sondomaine.fr'}]
### test +ieurs usilisateurs ###

def test_case_in_email_users(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [{'id': '001', 'email': 'khatira@sondomaine.fr'},{'id': '011', 'email': 'khatira_KHATIRA@sondomaine.fr'}]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
   
    users = user_service.list_users()

    assert users == [{'id': '001', 'email': 'khatira@sondomaine.fr'},{'id': '011', 'email': 'khatira_khatira@sondomaine.fr'}]



"""
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
"""