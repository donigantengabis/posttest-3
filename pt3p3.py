import os
import time
from prettytable import PrettyTable

os.system("cls")

waduh = input("Masukkan username : ")
wahah = input("Masukkan password : ")

class Node:
    def __init__(self, channel, next_node=None):
        self.channel = channel
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.history = []

    def add_channel(self, channel):
        new_node = Node(channel)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        self.history.append(f"Added channel {channel}")

    def print_channels(self):
        if not self.head:
            print("There are no channels.")
        else:
            table = PrettyTable()
            table.field_names = ["Channel"]
            current_node = self.head
            while current_node:
                table.add_row([current_node.channel])
                current_node = current_node.next_node
            print(table)

        self.history.append("Viewed channel list")

    def update_channel(self, old_channel, new_channel):
        if not self.head:
            print("There are no channels to update.")
        else:
            current_node = self.head
            while current_node:
                if current_node.channel == old_channel:
                    current_node.channel = new_channel
                    self.history.append(f"Updated channel {old_channel} to {new_channel}")
                    break
                current_node = current_node.next_node
            else:
                print(f"{old_channel} not found in channel list.")

    def delete_channel(self, channel):
        if not self.head:
            print("There are no channels to delete.")
        elif self.head.channel == channel:
            self.head = self.head.next_node
            self.history.append(f"Deleted channel {channel}")
        else:
            previous_node = self.head
            current_node = self.head.next_node
            while current_node:
                if current_node.channel == channel:
                    previous_node.next_node = current_node.next_node
                    self.history.append(f"Deleted channel {channel}")
                    break
                previous_node = current_node
                current_node = current_node.next_node
            else:
                print(f"{channel} not found in channel list.")

    def view_history(self):
        table = PrettyTable()
        table.field_names = ["Action"]
        for action in self.history:
            table.add_row([action])
        print(table)

linked_list = LinkedList()

while True:
    print("\nMENU")
    print("1. View channel list")
    print("2. Add channel")
    print("3. Update channel")
    print("4. Delete channel")
    print("5. View history")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        os.system("cls")
        linked_list.print_channels()
        time.sleep(2)
        os.system("cls")
    elif choice == "2":
        channel = input("Enter channel name: ")
        print("Done")
        linked_list.add_channel(channel)
        time.sleep(2)
        os.system("cls")

    elif choice == "3":        
        old_channel = input("Enter old channel name: ")
        new_channel = input("Enter new channel name: ")
        print("Done")
        linked_list.update_channel(old_channel, new_channel)
        time.sleep(2)
        os.system("cls")
    elif choice == "4":
        channel = input("Enter channel name: ")
        print("Done")
        linked_list.delete_channel(channel)
        time.sleep(2)
        os.system("cls")
    elif choice == "5":
        os.system("cls")
        linked_list.view_history()
        time.sleep(2)
        os.system("cls")
    elif choice == "6":
        os.system("cls")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
