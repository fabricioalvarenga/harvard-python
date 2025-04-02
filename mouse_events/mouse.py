from pynput import mouse

def main():
    with mouse.Listener(on_move = on_move, on_click = on_click) as listener:
        listener.join()


def on_move(x, y):
    print(f"{x}, {y}")


def on_click(x, y, button, pressed):
    if pressed:
        return False


if __name__ == "__main__":
    main()
