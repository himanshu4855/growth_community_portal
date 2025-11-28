import uuid
import time

members = []

def dashboard():
    while True:
        main_menu()
        choice = input("Enter your choice : ")
        
        if choice.isdigit():
           choice = int(choice)
        else:
            print("\nInvalid choice! Try again.\n")
            continue

        if choice == 1:
            register_member()
        elif choice == 2:
            view_members()
        elif choice == 3:
            exit_portal()
            break
        else:
            print("\nInvalid choice! Try again.\n")

def main_menu():
    print("\n──────────────────────────────────────────────")
    print("        COMMUNITY REGISTRATION PORTAL")
    print("──────────────────────────────────────────────\n")
    print("1. Join the Community")
    print("2. View Members")
    print("3. Exit\n")

def register_member():
    member_record = {}

    print("\n──────────────────────────────────────────────")
    print("                 USER DETAILS")
    print("──────────────────────────────────────────────\n")

    while True:
        name = input("Enter your Name: ").strip().title()
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid Name! Only alphabets allowed.\n")

    while True:
        address = input("Enter your Address: ").strip().title()
        if address.replace(" ", "").isalnum():
            break
        else:
            print("Invalid Address! Only letters and numbers allowed.\n")

    member_id = uuid.uuid4().hex[:12].upper()
    print("\nGenerating your Unique ID…")
    print("Your Member ID:", member_id)

    while True:
        print("\n1. Next")
        print("2. Cancel\n")
        next_choice = input("Enter your choice (1/2): ")

        if next_choice.isdigit():
           next_choice = int(next_choice)
        else:
            print("\nInvalid choice! Try again.\n")
            continue
        
        if next_choice == 1:
            break
        elif next_choice == 2:
            print("\nReturning to main menu...\n")
            return
        else:
            print("Invalid choice! Try again.\n")

    docs = upload_documents()

    if docs is None:
        print("\nForm submission cancelled.\n")
        return

    member_record["id"] = member_id
    member_record["name"] = name
    member_record["address"] = address
    member_record["documents"] = docs

    members.append(member_record)
    final_submission(member_id)

def upload_documents():
    documents = {}

    print("\n──────────────────────────────────────────────")
    print("               DOCUMENT UPLOAD")
    print("──────────────────────────────────────────────\n")
    print("Upload 3 documents. Names must be unique.\n")

    for i in range(1, 4):
        while True:
            print(f"[ Document {i} ]")
            doc_name = input("Name: ").strip().title()

            if not doc_name.replace(" ", "").isalpha():
                print("Invalid name! Only alphabets allowed.\n")
                continue

            if doc_name in documents:
                print("This document name already exists! Choose another.\n")
                continue

            doc_link = input("Link: ").strip()

            print("Uploading…")
            time.sleep(2)
            print("Done.\n")

            documents[doc_name] = doc_link
            break

    while True:
        print("1. Submit")
        print("2. Cancel\n")
        submit_choice = input("Enter your choice (1/2): ")

        if submit_choice.isdigit():
           submit_choice = int(submit_choice)
        else:
            print("\nInvalid choice! Try again.\n")
            continue
        
        if submit_choice == 1:
            return documents
        elif submit_choice == 2:
            return None
        else:
            print("Invalid choice! Try again.\n")

def final_submission(member_id):
    print("\n──────────────────────────────────────────────")
    print("            REGISTRATION SUCCESSFUL ")
    print("──────────────────────────────────────────────\n")
    print("You are now a member of our community.\n")
    print("Your Member ID:")
    print(member_id, "\n")
    print("Join our WhatsApp group:")
    print("https://chat.whatsapp.com/FAKE-LINK-123\n")

    time.sleep(2)
    print("Returning to main menu...\n")

def view_members():
    print("\n──────────────────────────────────────────────")
    print("                 MEMBER LIST")
    print("──────────────────────────────────────────────\n")

    if not members:
        print("No members found.\n")
        input("(Press Enter to return)")
        return

    for index, record in enumerate(members, start=1):
        print(f"Member #{index}")
        print("ID:", record["id"])
        print("Name:", record["name"])
        print("Address:", record["address"])
        print("Documents:")
        
        for doc_name, doc_link in record["documents"].items():
            print(f"  - {doc_name} -> {doc_link}")
        
        print("\n")

    input("(Press Enter to return)")

def exit_portal():
    print("EXIT...")
    print("Thank you for using the portal.\n")

dashboard()