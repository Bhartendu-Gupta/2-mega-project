import pyautogui
import pyperclip
import time

# Wait a moment to give you time to switch to the right window
time.sleep(3)

# Click on the icon at (1071, 1047)
pyautogui.click(1071, 1047)

# Wait a moment for the click action to register
time.sleep(1)

# Click and drag to select text from (480, 144) to (1137, 944)
pyautogui.mouseDown(480, 144)
pyautogui.moveTo(712, 917, duration=1)  # You can adjust the duration for a smoother drag
pyautogui.mouseUp()

# Wait a moment for the selection to complete
time.sleep(0.5)

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Wait a moment for the copy action to complete
time.sleep(0.5)

# Retrieve the copied text from the clipboard
copied_text = pyperclip.paste()

# Print the copied text (or use it as needed)
print(copied_text)
