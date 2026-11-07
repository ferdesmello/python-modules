#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List
from datetime import datetime
from enum import Enum


class CrewRanks(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_data_validation(self) -> "SpaceMission":
        if (not self.mission_id.startswith("M")):
            raise ValueError("Mission ID must start with 'M'")

        has_leader: bool = any(
            member.rank in [CrewRanks.CAPTAIN, CrewRanks.COMMANDER]
            for member in self.crew
            )
        if (not has_leader):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if (self.duration_days > 365):
            half: float = len(self.crew) / 2
            experienced_crew_count: int = len(
                [member for member in self.crew
                 if member.years_experience >= 5])
            if (experienced_crew_count < half):
                raise ValueError(
                    "For missions longer than a year, at least half "
                    "of the crew must have 5+ years of experience"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")
    print("Valid mission created:")

    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.strptime("2024-07-15T14:30:00",
                                          "%Y-%m-%dT%H:%M:%S"),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C_001",
                    name="Sarah Connor",
                    rank=CrewRanks.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=15,
                    is_active=True
                ),
                CrewMember(
                    member_id="C_002",
                    name="John Smith",
                    rank=CrewRanks.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="C_003",
                    name="Alice Johnson",
                    rank=CrewRanks.OFFICER,
                    age=40,
                    specialization="Engineering",
                    years_experience=8,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Destination: {mission1.destination}")
        print(f"Duration: {mission1.duration_days} days")
        print(f"Budget: ${mission1.budget_millions}M")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")
        for member in mission1.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print()
    print("=======================================")
    print("Expected validation error:")

    try:
        crew_member_1: CrewMember = CrewMember(
            member_id="G_007",
            name="Luke Skywalker",
            rank=CrewRanks.CADET,
            age=25,
            specialization="Landing Operations",
            years_experience=10,
            is_active=True
        )
        crew_member_2: CrewMember = CrewMember(
            member_id="G_008",
            name="Jane Doe",
            rank=CrewRanks.LIEUTENANT,
            age=30,
            specialization="Piloting",
            years_experience=2,
            is_active=True
        )
        crew_member_3: CrewMember = CrewMember(
            member_id="G_013",
            name="Bob Johnson",
            rank=CrewRanks.OFFICER,
            age=55,
            specialization="Electronics",
            years_experience=10,
            is_active=True
        )
        mission2 = SpaceMission(
            mission_id="M2026_VENUS",
            mission_name="Venus Exploration",
            destination="Venus",
            launch_date=datetime.strptime("2026-02-20T09:00:00",
                                          "%Y-%m-%dT%H:%M:%S"),
            duration_days=1500,
            crew=[
                crew_member_1,
                crew_member_2,
                crew_member_3
            ],
            mission_status="planned",
            budget_millions=3700.0
        )
        print(f"Mission: {mission2.mission_name}")
        print(f"ID: {mission2.mission_id}")
        print(f"Destination: {mission2.destination}")
        print(f"Duration: {mission2.duration_days} days")
        print(f"Budget: ${mission2.budget_millions}M")
        print(f"Crew size: {len(mission2.crew)}")
        print("Crew members:")
        for member in mission2.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
