import random

def check_room(room):
    if r_s[room] == "dirty":
        print(f"{room} is dirty")
        r_s[room] = "clean"  # Clean the room
        print(f"{room} is cleaned")
        return True  # Room was dirty and has now been cleaned

    if r_s[room] == "clean":
        print(f"{room} is clean")
        return False  # Room was already clean

    return False

# checking if all the rooms are clean
def all_rooms_clean():
    return all(status == "clean" for status in r_s.values())



# Start point
r_s = {"room1": "clean", "room2": "dirty"}
room = ["room1", "room2"]

on_status = input("Do you want to turn ON the cleaner? (yes/no) ").lower().strip()

if on_status == "yes":
    while True:  # Continue until both rooms are clean
        for r in room:
            check_room(r)  # Check and clean the current room

            # After checking, randomly assign the status for the room
            r_s[r] = random.choice(["dirty", "clean"])

        # Check if all rooms are clean after processing both rooms
        if all_rooms_clean():
            print("Both rooms are clean. Exiting.")
            break

else:
    print("Cleaner is off.")
