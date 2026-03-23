from dataclasses import dataclass, field
from typing import List
from datetime import date


from demoqa.pages.registration_page import Hobbies


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
    mobile: str

    gender: str  # "Male" | "Female" | "Other"

    date_of_birth: date

    subjects: List[str] = field(default_factory=list)
    hobbies: List[Hobbies] = field(default_factory=list)

    picture: str = ""
    address: str = ""

    state: str = ""
    city: str = ""


user = UserPractiseForm(
    first_name="Kurva",
    last_name="Bobr",
    email="kurvabobr@gmail.com",
    mobile="1234567890",
    gender="Male",
    # day="19",
    # month="April",
    # year="2022",
    date_of_birth=date(2022, 4, 19),
    subjects=["Computer Science", 'English'],
    hobbies=[Hobbies.MUSIC],
    picture="robert.webp",
    address="202-2 Dunsheath Way",
    state="NCR",
    city="Noida"
)