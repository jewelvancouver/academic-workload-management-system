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

def display_workloads(filepath="data/workload.txt"):
    """Reads and prints all workloads from the text file."""
    print("\n--- Current Academic Workload ---")
    with open(filepath, "r") as file:
        for line in file:
            task, course, deadline, status = line.strip().split(",")
            print(f"Task: {task} | Course: {course} | Due: {deadline} | Status: {status}")
