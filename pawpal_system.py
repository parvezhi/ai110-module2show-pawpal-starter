from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional, Dict


@dataclass
class Task:
    description: str
    time: str  # "HH:MM"
    pet_name: str
    frequency: Optional[str] = None  # None, "daily", "weekly"
    completed: bool = False

    def mark_complete(self) -> Optional["Task"]:
        """Mark this task as complete and, if recurring, return the next occurrence."""
        self.completed = True

        if self.frequency is None:
            return None

        # Parse current time as today + HH:MM
        now = datetime.now()
        hour, minute = map(int, self.time.split(":"))
        current_dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if self.frequency == "daily":
            next_dt = current_dt + timedelta(days=1)
        elif self.frequency == "weekly":
            next_dt = current_dt + timedelta(weeks=1)
        else:
            return None

        next_time = next_dt.strftime("%H:%M")
        return Task(
            description=self.description,
            time=next_time,
            pet_name=self.pet_name,
            frequency=self.frequency,
            completed=False,
        )


@dataclass
class Pet:
    name: str
    species: Optional[str] = None
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: Dict[str, Pet] = {}

    def add_pet(self, pet: Pet) -> None:
        """Register a new pet under this owner."""
        self.pets[pet.name] = pet

    def get_pet(self, name: str) -> Optional[Pet]:
        """Retrieve a pet by name."""
        return self.pets.get(name)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        tasks: List[Task] = []
        for pet in self.pets.values():
            tasks.extend(pet.get_tasks())
        return tasks


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def sort_by_time(self) -> List[Task]:
        """Return all tasks sorted by time."""
        tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(
        self,
        pet_name: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> List[Task]:
        """Filter tasks by pet name and/or completion status."""
        tasks = self.owner.get_all_tasks()
        result: List[Task] = []

        for task in tasks:
            if pet_name is not None and task.pet_name != pet_name:
                continue
            if completed is not None and task.completed != completed:
                continue
            result.append(task)

        return result

    def detect_conflicts(self) -> List[List[Task]]:
        """
        Detect conflicts where two or more tasks share the same time.
        Returns a list of lists, each inner list being conflicting tasks.
        """
        tasks = self.owner.get_all_tasks()
        by_time: Dict[str, List[Task]] = {}

        for task in tasks:
            by_time.setdefault(task.time, []).append(task)

        conflicts = [group for group in by_time.values() if len(group) > 1]
        return conflicts

    def mark_task_complete(self, task: Task) -> Optional[Task]:
        """
        Mark a task complete and, if recurring, return the new task instance.
        Caller is responsible for adding the new task to the appropriate pet.
        """
        return task.mark_complete()
