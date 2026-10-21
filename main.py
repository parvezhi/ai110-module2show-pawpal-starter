from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(tasks):
    print("Today's Schedule:")
    for task in tasks:
        conflict_marker = ""
        print(f"- {task.time} | {task.description} ({task.pet_name}){conflict_marker}")


def main():
    owner = Owner("Parvez")

    bella = Pet(name="Bella", species="Dog")
    max_pet = Pet(name="Max", species="Cat")

    owner.add_pet(bella)
    owner.add_pet(max_pet)

    bella.add_task(Task(description="Morning walk", time="08:00", pet_name="Bella", frequency="daily"))
    bella.add_task(Task(description="Feed breakfast", time="09:00", pet_name="Bella"))
    max_pet.add_task(Task(description="Feed breakfast", time="09:00", pet_name="Max"))
    bella.add_task(Task(description="Medication", time="18:00", pet_name="Bella", frequency="daily"))

    scheduler = Scheduler(owner)

    sorted_tasks = scheduler.sort_by_time()
    print_schedule(sorted_tasks)

    conflicts = scheduler.detect_conflicts()
    for group in conflicts:
        timestr = group[0].time
        names = ", ".join(f"{t.description} ({t.pet_name})" for t in group)
        print(f"⚠️ Conflict at {timestr}: {names}")

    # Demonstrate recurrence
    daily_task = bella.tasks[0]
    new_task = scheduler.mark_task_complete(daily_task)
    if new_task:
        bella.add_task(new_task)
        print(f"Recurring task created: {new_task.description} for {new_task.pet_name} at {new_task.time}")


if __name__ == "__main__":
    main()
