from dataclasses import dataclass


@dataclass
class TestUser:
    full_name: str
    email: str
    current_address: str
