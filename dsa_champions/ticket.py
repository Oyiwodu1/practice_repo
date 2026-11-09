import json

def create_ticket():
    tickets = []
    while True:
        title = input("Enter ticket title: ").strip()
        if title == "":
            print("Enter a valid ticket title!")
            continue

        valid_category = ["Network", "Software", "Hardware", "Other"]
        category = input("Enter category(network/hardware/software/other): ").strip().title()
        if category not in valid_category:
            print("Enter a valid category")
            continue

        ticket = {
            "Title": title,
            "Category": category,
            "Status": "Open"
        }
        tickets.append(ticket)

        print("Ticket created Successfully")
        print(ticket)

        again = input("Create another ticket? (yes/no): ").strip().lower()
        if again != "yes":
            break

    with open("tickets.json", "w")as file:
        json.dump(tickets, file, indent=4)

    return tickets
create_ticket()