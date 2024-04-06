#The Superhero's Quest: The Lost City of Infinity 🦸‍♀️🌟

print("🌟🦸‍♂️ Welcome to the Superhero's Quest! 🦸‍♀️🌟")
print("You are standing at a crossroad, ready for an epic adventure.")
path = input("Will you go left or right? ").lower()

if path == "left":
    choice = input("Do you want to swim across the river or wait for the mystical boat? ").lower()
    if choice == "boat":
        print("🚤 The Boat is approaching! You step aboard, heart racing.")
        door = input("Three doors stand before you: 'red', 'blue', or 'yellow'. Which one do you choose? ").lower()
        if door == "red":
            print("🔥 The door bursts into flames! You've been scorched. Game Over!")
        elif door == "blue":
            print("🐉 A ferocious beast lunges at you! You're no match. Game Over!")
        elif door == "yellow":
            print("🌟 The door opens to reveal a dazzling treasure room! You win!!")
        else:
            print("⚠️ Invalid choice! The magical forces disintegrate you. Game Over!")
    else:
        print("🐟 Suddenly, a giant Trout leaps from the water! You're no match. Game Over!")

else:
    print("🕳️ You stumble into a mysterious hole and fall into darkness. Game Over!")

print("\n🌟🦸‍♂️ Thank you for playing The Superhero's Quest! 🦸‍♀️🌟")
