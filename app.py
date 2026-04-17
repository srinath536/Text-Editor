import msvcrt

data_buffer = []
undo_buffer = []

print("Start typing (ESC to save & exit):")

while True:
    key = msvcrt.getch()

    # EXIT
    if key == b'\x1b':  # ESC
        break

    # BACKSPACE
    elif key == b'\x08':
        if data_buffer:
            removed_char=data_buffer.pop()
            undo_buffer.append(removed_char)
            print('\b \b', end='', flush=True)

    # UNDO
    elif key == b'\x1A':  # CTRL+Z
        if undo_buffer:
            removed_char = undo_buffer.pop()
            data_buffer.append(removed_char)
            print(removed_char, end='', flush=True)
    
    # ENTER
    elif key == b'\r':
        data_buffer.append('\n')
        print()

    else:
        try:
            char = key.decode('utf-8')
            data_buffer.append(char)
            print(char, end='', flush=True)
        except:
            continue

# SAVE FILE
with open("new.txt", "w") as file:
    file.write("".join(data_buffer))

print("\n\nFile saved as new.txt ✅")