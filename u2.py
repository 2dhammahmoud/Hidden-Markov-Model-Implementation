import time
import random
import threading

def node(name, inbox, running):
    while running["value"]:
        if inbox:
            msg = inbox.pop(0)
            print(f"{name} received: {msg}")
            time.sleep(random.uniform(0.3, 1.5))
        else:
            time.sleep(0.1)

inboxes = {f"Node {i}": [] for i in ["A","B","C","D","E"]}
running = {"value": True}

for name, inbox in inboxes.items():
    threading.Thread(target=node, args=(name, inbox, running), daemon=True).start()

END_TIME = time.time() + 15  # stop after 15 seconds

while time.time() < END_TIME:
    msg = f"Ping at {time.time():.2f}"
    for inbox in inboxes.values():
        inbox.append(msg)
    time.sleep(2)

running["value"] = False
print("\nSimulation stopped after 15 seconds.")
