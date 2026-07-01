# MeltFocus

MeltFocus is a browser-based focus timer that replaces traditional countdowns with a realistic melting simulation. Instead of watching numbers tick down, users observe a candle, an ice cube, or both gradually melt until a hidden study session ends.

## Development

The application's core logic and behaviour were first designed in Python. The final web version was then outsourced for implementation in HTML, CSS, and JavaScript based on that Python design and specification.

## Features

- Choose between a **Candle**, **Ice Cube**, or **Both**.
- Set a **minimum and maximum** study duration using hours, minutes, and seconds.
- A hidden duration is randomly selected within the chosen range (inclusive) and never revealed until the session finishes.
- Real-time procedural melting animations built entirely with HTML, CSS, and JavaScript—no images, GIFs, videos, or external libraries.
- Candle simulation featuring:
  - Flickering flame
  - Gradually shortening wax body
  - Wax drips
  - Growing wax puddle
- Ice simulation featuring:
  - Translucent melting cube
  - Uneven shape deformation
  - Falling water droplets
  - Expanding water puddle with ripples
- Descriptive progress captions instead of countdown timers.
- "Melt Again" to start another randomly timed session.
- "Change Settings" to choose a new object or time range.
- Responsive dark-themed interface designed for distraction-free studying.

## Purpose

MeltFocus encourages deep focus by removing the temptation to constantly check a countdown timer. Instead, users estimate their progress naturally by observing the gradual melting of the chosen object, creating a calmer and more immersive study experience.

## Technologies

- HTML5
- CSS3
- Vanilla JavaScript
- Python (application logic and initial design)
