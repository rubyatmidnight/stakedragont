import random
import time
import keyboard

print("\nReference:")
print("\n1: 2.94x")
print("\n2: 8.82x")
print("\n3: 26.46x")
print("\n4: 79.38x")
print("\n5: 238.14x")
print("\n6: 714.42x")
print("\n7: 2143.26x")
print("\n8: 6429.78x")
print("\n9: 19,289.34x")
print("\n ")

pathLength = int(input("Enter path length, 1-9: "))  

def generatePath():
    directionMap = {0: "L", 1: "M", 2: "R"}
    return ''.join(directionMap[random.randint(0, 2)] for _ in range(pathLength))

def simulateButtonPress(key):
    keyboard.press_and_release(key)
    print(f"Keypress: {key}")
    time.sleep(0.4)

def printPathSummary(path):
    print(f"\nPath: {path}")


def runSimulation():
    path = generatePath()
    printPathSummary(path)
    
    print("\nFollowing path order: . Press 'Esc' to stop.")
    for direction in path:
        if keyboard.is_pressed('esc'):
            print("Stopping.")
            return False
        simulateButtonPress("1" if direction == "L" else "2" if direction == "M" else "3")
    
    time.sleep(0.25)
    simulateButtonPress('w')
    print("Cashing out... or restarting: ")
    time.sleep(0.75)
    
    # Press spacebar to restart
    simulateButtonPress('space')
    print("Starting next round: ")
    time.sleep(0.75)

    
    return True

print("Press 'Enter' to start. Press 'Esc' to stop.")
print("This uses your keyboard inputs, so you need to stay focused on the page.")

keyboard.wait('enter')

try:
    while True:
        if not runSimulation():
            break
except KeyboardInterrupt:
    print("Pausing.")

print("Terminating.")
