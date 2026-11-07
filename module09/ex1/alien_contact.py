#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact(self) -> "AlienContact":
        if (not self.contact_id.startswith("AC")):
            raise ValueError("Contact ID must start with 'AC'")

        if (
            self.contact_type == ContactType.PHYSICAL and not
            self.is_verified
        ):
            raise ValueError("Physical contacts must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC and
            self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if (
            self.signal_strength > 7.0 and not
            self.message_received
        ):
            raise ValueError(
                "Strong signals should include received messages"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    try:
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print(f"ID: {contact1.contact_id}")
        print(f"Type: {contact1.contact_type.value}")
        print(f"Location: {contact1.location}")
        print(f"Signal: {contact1.signal_strength}/10")
        print(f"Duration: {contact1.duration_minutes} minutes")
        print(f"Witnesses: {contact1.witness_count}")
        print(f"Message: {contact1.message_received}")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print()
    print("=======================================")
    print("Expected validation error:")

    try:
        contact2 = AlienContact(
            contact_id="AC_2026_007",
            timestamp=datetime.now(),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=7.2,
            duration_minutes=30,
            witness_count=1,
            message_received="Sightings of unidentified flying objects",
            is_verified=False
        )
        print(f"ID: {contact2.contact_id}")
        print(f"Type: {contact2.contact_type.value}")
        print(f"Location: {contact2.location}")
        print(f"Signal: {contact2.signal_strength}/10")
        print(f"Duration: {contact2.duration_minutes} minutes")
        print(f"Witnesses: {contact2.witness_count}")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
