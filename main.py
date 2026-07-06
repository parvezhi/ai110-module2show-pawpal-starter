from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def build_demo_owner() -> Owner:
    owner = Owner(name="Demo Owner")

    pet1 = Pet(name="Buddy", species="Dog")
    pet2 = Pet(name="Mittens", species="Cat")

    now = datetime.now()
    pet1.add_task(Task(description="Morning walk", time=now + timedelta(minutes=30)))
    pet1.add_task(Task(description="Feed breakfast", time=now + timedelta(minutes=10)))
    pet2.add_task(Task(description="Give medication", time=now + timedelta(minutes=20), frequency="daily"))

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    return owner


def print_today_schedule(scheduler: Scheduler) -> None:
    tasks = scheduler.get_today_tasks()
    tasks = scheduler.sort_by_time(tasks)
    conflicts = scheduler.detect_conflicts(tasks)

    print("=== Today's Schedule ===")
    for task in tasks:
        time_str = task.time.strftime("%H:%M")
        status = "✅" if task.completed else "⏳"
        print(f"{time_str} - {task.description} ({status})")

    if conflicts:
        print("\n=== Conflicts Detected ===")
        for c in conflicts:
            print(f"⚠️ {c}")


if __name__ == "__main__":
    owner = build_demo_owner()
    scheduler = Scheduler(owner)
    print_today_schedule(scheduler)
