from dog import Dog
from enclosure import Enclosure
from kennel_company import Kennel_Company
import pytest


def load_enclosure_stub(self):
    return [
        Enclosure(1, 6, 5),
        Enclosure(2, 12, 7),
        Enclosure(3, 10, 6)
    ]
def add_occupant_temp(self, dog):
    self.occupants.append(dog)

@pytest.fixture
def company(monkeypatch):
    monkeypatch.setattr(Kennel_Company, "load_enclosures", load_enclosure_stub)
    kennel_company = Kennel_Company()
    return kennel_company


def test_book_dogs(monkeypatch, company):
    dog1 = Dog("mark", "karl", 10, "husky", "eats food")
    dog2 = Dog("boris", "jason", 5, "german shepherd", "drinks water")
    company.book_dog(dog1)
    company.book_dog(dog2)
    monkeypatch.setattr(Enclosure, "add_occupant", add_occupant_temp)
    monkeypatch.setattr(Enclosure, "check_suitability", lambda self, dog: True)
    assert company.spaces_left() == 18
