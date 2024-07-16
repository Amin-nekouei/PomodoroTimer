# Pomodoro Timer

## Overview

The **Pomodoro Timer** is a productivity tool that uses the Pomodoro Technique to help manage time and improve focus. The Pomodoro Technique involves working for a set period (usually 25 minutes) and then taking a short break. After a few cycles, a longer break is taken. This project is built using Python's `tkinter` library for the GUI and `pygame` for playing sound notifications.

## Features

- **Work and Break Cycles**: Work for 25 minutes followed by a short break (5 minutes) and a long break (30 minutes) after 8 cycles.
- **Sound Notifications**: Plays sound notifications at the start of work, short breaks, and long breaks.
- **Visual Timer**: Displays a visual countdown timer with a tomato-themed UI.
- **Checkmarks**: Shows checkmarks to represent completed cycles.



## Usage

2. **Controls**:
    - **Start Button**: Starts the work or break timer based on the current cycle.
    - **Reset Button**: Resets the timer and the repetition counter.

3. **Sound Notifications**:
    - Ensure your speakers are on to hear the sound notifications for work periods, short breaks, and long breaks.

## Code Explanation

- **Constants**: Define colors, font names, and time intervals used in the application.
- **Functions**:
  - `play_sound(sound_file)`: Plays the specified sound file.
  - `start()`: Starts the timer and manages work/break cycles.
  - `reset()`: Resets the timer and repetition counter.
  - `count_down(second)`: Handles the countdown logic and updates the UI.
- **UI Setup**: Configures the Tkinter window and its elements, including labels, buttons, and the canvas for the timer display.
