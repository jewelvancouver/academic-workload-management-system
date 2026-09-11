class Workload:
    def __init__(self, task_name, course, deadline, status="Pending"):
        self.task_name = task_name
        self.course = course
        self.deadline = deadline
        self.status = status

    def display(self):
        print(f"Task: {self.task_name}")
        print(f"Course: {self.course}")
        print(f"Deadline: {self.deadline}")
        print(f"Status: {self.status}")
        print("-" * 30)

    def to_file_format(self):
        return f"{self.task_name}|{self.course}|{self.deadline}|{self.status}\n"
def save_workload(self, filepath="data/workload.txt"):
    """Saves the current workload entry to a text file."""
    with open(filepath, "a") as file:
        file.write(f"{self.task_name},{self.course},{self.deadline},{self.status}\n")
