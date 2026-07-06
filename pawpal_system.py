from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: datetime
    frequency: str = "once"  # "once", "daily"
    completed: bool = False

    def mark_complete(self) -> Optional["Task"]:
        """Mark this task as complete. Return new task if recurring."""
        self.completed = True
        if self.frequency.lower() == "daily":
            new_time = self.time + timedelta(days=1)
            return Task(
                description=self.description,
                time=new_time,
                frequency=self.frequency,
                completed=False,
            )
        return None


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize scheduler with an owner."""
        self.owner = owner

    def get_today_tasks(self) -> List[Task]:
        """Return tasks scheduled for today."""
        today = datetime.now().date()
        return [
            task for task in self.owner.get_all_tasks()
            if task.time.date() == today
        ]

    def sort_by_time(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """Return tasks sorted by time."""
        if tasks is None:
            tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda t: t.time)

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks for a specific pet."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                return pet.get_tasks()
        return []

    def filter_by_status(self, completed: bool) -> List[Task]:
        """Return tasks filtered by completion status."""
        return [
            task for task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def detect_conflicts(self, tasks: Optional[List[Task]] = None) -> List[str]:
        """Detect tasks with the exact same time."""
        if tasks is None:
            tasks = self.owner.get_all_tasks()
        conflicts = []
        seen = {}
        for task in tasks:
            key = task.time
            if key in seen:
                conflicts.append(
                    f"Conflict: '{task.description}' and '{seen[key].description}' at {task.time}"
                )
            else:
                seen[key] = task
        return conflicts
