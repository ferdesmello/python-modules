from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=======================================")
    print("Valid station created:")

    try:
        station1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-11-05T05:15:00",
            is_operational=True,
            notes="Operational"
        )
        print(f"ID: {station1.station_id}")
        print(f"Name: {station1.name}")
        print(f"Crew: {station1.crew_size} people")
        print(f"Power: {station1.power_level}%")
        print(f"Oxygen: {station1.oxygen_level}%")
        print(f"Status: {station1.is_operational}")
        print(f"Notes: {station1.notes}")
    except ValidationError as e:
        print("Error creating station1:", e)

    print()
    print("========================================")
    print("Expected validation error:")

    try:
        station2 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-11-05T05:15:00",
            is_operational=True,
            notes="Operational"
        )
        print("Valid station created:")
        print(f"ID: {station2.station_id}")
        print(f"Name: {station2.name}")
        print(f"Crew: {station2.crew_size} people")
        print(f"Power: {station2.power_level}%")
        print(f"Oxygen: {station2.oxygen_level}%")
        print(f"Status: {station2.is_operational}")
        print(f"Notes: {station2.notes}")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
