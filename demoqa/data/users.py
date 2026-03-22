from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    current_address: str


simple_user = User(
    full_name="Bobr Kurva",
    email="bkurva@gmail.com",
    current_address="Dunsheath Way 777, MArkham, ON",
)

@dataclass
class UserPractiseForm:
    first_name: str
    last_name: str
    email: str
    current_address: str
