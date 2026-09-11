from workload import Workload

FILENAME = "data/workload.txt"


def add_workload():
    print("\nAdd Academic Workload")

    task_name = input("Enter task name: ")
    course = input("Enter course/module: ")
    deadline = input("Enter deadline: ")

    workload = Workload(task_name, course, deadline)

    try:
        with open(FILENAME, "a") as file:
            file.write(workload.to_file_format())

        print("Workload added successfully.")

    except Exception as error:
        print("An error occurred:", error)


def view_workload():
    print("\nAcademic Workload")

    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No workload records found.")
            return

        for record in records:
            data = record.strip().split("|")

            if len(data) == 4:
                workload = Workload(
                    data[0],
                    data[1],
                    data[2],
                    data[3]
                )

                workload.display()

    except FileNotFoundError:
        print("No workload file found yet.")

    except Exception as error:
        print("An error occurred:", error)


def main():
    while True:
        print("\n===== Academic Workload Management System =====")
        print("1. Add workload")
        print("2. View workload")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_workload()

        elif choice == "2":
            view_workload()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

try:
    display_workloads()
except FileNotFoundError:
    print("Error: Workload file not found. Creating a new record...")
except ValueError:
    print("Error: Invalid data format in workload file.")
    
