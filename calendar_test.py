from ics import Calendar, Event
from datetime import datetime, timedelta

# Create a calendar
calendar = Calendar()

# Define start date for the learning plan
start_date = datetime.today()

# Day-wise learning tasks
tasks = [
    # Week 1: Basics and Fundamentals
    ("Introduction to Rust, setting up the environment", 2),
    ("Variables, types, and functions", 3),
    ("Ownership, borrowing, and lifetimes", 2),

    # Week 2: Control Flow and Error Handling
    ("Conditionals and loops", 2),
    ("Pattern matching and enums", 3),
    ("Error handling with Result and Option", 2),

    # Week 3: Collections and Iterators
    ("Arrays, vectors, and strings", 2),
    ("HashMaps and Sets", 2),
    ("Iterators and closures", 3),

    # Week 4: Modules and Project Structure
    ("Modules and packages", 2),
    ("Testing and debugging", 2),
    ("Building a small Rust project", 3),

    # Week 5-6: Intermediate Rust Concepts
    ("Advanced ownership and lifetimes", 3),
    ("Traits and generics", 3),
    ("Smart pointers and memory management", 3),

    # Week 7-8: Concurrency and Asynchronous Programming
    ("Threads and shared state", 3),
    ("Channels and messaging", 3),
    ("Async/Await in Rust", 3),

    # Week 9-10: Systems Programming
    ("Working with files and I/O", 3),
    ("Networking and web servers", 3),
    ("FFI and unsafe Rust", 3),

    # Week 11-12: Advanced Projects and Optimization
    ("Building a CLI tool", 3),
    ("Creating a web API with Rocket or Actix", 3),
    ("Profiling and performance optimization", 3),
    ("Final project wrap-up", 2),
]

# Create calendar events
current_date = start_date
for task, duration in tasks:
    for _ in range(duration):
        event = Event()
        event.name = f"Rust Learning: {task}"
        event.begin = current_date.strftime("%Y-%m-%d 09:00:00")
        event.end = (current_date + timedelta(hours=1)).strftime("%Y-%m-%d 10:00:00")
        calendar.events.add(event)
        current_date += timedelta(days=1)

# Save to .ics file
calendar_path = "/workspaces/ElementalAI/rust_learning_plan.ics"
with open(calendar_path, "w") as f:
    f.writelines(calendar)

calendar_path
