import json
from datetime import datetime

# Ticketing System Database
tickets = {}
ticket_counter = 1000

def create_ticket(user_name, email, issue_title, issue_description, priority="Medium"):
    """Create a new support ticket"""
    global ticket_counter
    ticket_counter += 1
    
    ticket = {
        "ticket_id": ticket_counter,
        "user_name": user_name,
        "email": email,
        "title": issue_title,
        "description": issue_description,
        "priority": priority,
        "status": "Open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tickets[ticket_counter] = ticket
    return ticket_counter

def view_tickets(user_name=None):
    """View all tickets or tickets by user"""
    if not tickets:
        print("No tickets found.")
        return
    
    filtered_tickets = tickets
    if user_name:
        filtered_tickets = {k: v for k, v in tickets.items() if v["user_name"].lower() == user_name.lower()}
    
    if not filtered_tickets:
        print(f"No tickets found for {user_name}")
        return
    
    print("\n" + "="*80)
    print("TICKET LIST")
    print("="*80)
    for ticket_id, ticket in filtered_tickets.items():
        print(f"\nTicket ID: {ticket_id}")
        print(f"User: {ticket['user_name']} ({ticket['email']})")
        print(f"Title: {ticket['title']}")
        print(f"Status: {ticket['status']} | Priority: {ticket['priority']}")
        print(f"Created: {ticket['created_at']}")
        print("-" * 80)

def view_ticket_details(ticket_id):
    """View detailed information about a specific ticket"""
    if ticket_id not in tickets:
        print(f"Ticket {ticket_id} not found.")
        return
    
    ticket = tickets[ticket_id]
    print("\n" + "="*80)
    print(f"TICKET #{ticket_id} DETAILS")
    print("="*80)
    print(f"User Name: {ticket['user_name']}")
    print(f"Email: {ticket['email']}")
    print(f"Title: {ticket['title']}")
    print(f"Description: {ticket['description']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Status: {ticket['status']}")
    print(f"Created: {ticket['created_at']}")
    print(f"Updated: {ticket['updated_at']}")
    print("="*80 + "\n")

def update_ticket_status(ticket_id, new_status):
    """Update the status of a ticket"""
    valid_statuses = ["Open", "In Progress", "Resolved", "Closed"]
    
    if ticket_id not in tickets:
        print(f"Ticket {ticket_id} not found.")
        return False
    
    if new_status not in valid_statuses:
        print(f"Invalid status. Valid statuses: {', '.join(valid_statuses)}")
        return False
    
    tickets[ticket_id]["status"] = new_status
    tickets[ticket_id]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Ticket {ticket_id} status updated to '{new_status}'")
    return True

def close_ticket(ticket_id):
    """Close a ticket"""
    return update_ticket_status(ticket_id, "Closed")

def main():
    """Main menu for the ticketing system"""
    print("\n" + "="*80)
    print("WELCOME TO THE SUPPORT TICKETING SYSTEM")
    print("="*80 + "\n")
    
    while True:
        print("\nOptions:")
        print("1. Create a new ticket")
        print("2. View all tickets")
        print("3. View my tickets")
        print("4. View ticket details")
        print("5. Update ticket status")
        print("6. Close ticket")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == "1":
            print("\n--- CREATE NEW TICKET ---")
            user_name = input("Your name: ").strip()
            email = input("Your email: ").strip()
            title = input("Issue title: ").strip()
            description = input("Issue description: ").strip()
            priority = input("Priority (Low/Medium/High) [Default: Medium]: ").strip() or "Medium"
            
            ticket_id = create_ticket(user_name, email, title, description, priority)
            print(f"\n✓ Ticket created successfully! Your ticket ID is: {ticket_id}")
        
        elif choice == "2":
            view_tickets()
        
        elif choice == "3":
            user_name = input("Enter your name: ").strip()
            view_tickets(user_name)
        
        elif choice == "4":
            ticket_id = int(input("Enter ticket ID: ").strip())
            view_ticket_details(ticket_id)
        
        elif choice == "5":
            ticket_id = int(input("Enter ticket ID: ").strip())
            print("Valid statuses: Open, In Progress, Resolved, Closed")
            new_status = input("Enter new status: ").strip()
            update_ticket_status(ticket_id, new_status)
        
        elif choice == "6":
            ticket_id = int(input("Enter ticket ID to close: ").strip())
            close_ticket(ticket_id)
        
        elif choice == "7":
            print("\nThank you for using the Support Ticketing System. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()