# Harry Potter Invisible Cloak

This project implements the "Invisible Cloak" effect inspired by Harry Potter using computer vision techniques. It allows you to make any object covered by a specific color appear invisible in the video feed.

## Requirements

- Python 3
- OpenCV library (cv2)
- Numpy library

## Usage

1. Install the required libraries by running the following command:
>pip install opencv-python numpy


2. Run the `invisible_cloak.py` script:
>python invisible_cloak.py


3. A video feed from your default camera will open, showing the background capture phase. In this phase, move any object or person you want to make invisible out of the frame. Press the 'x' key to capture the background.

4. After capturing the background, the main video feed will open again. Place the object or person back into the frame, covering them with a cloth of the specified color (e.g., green).

5. The cloth-covered area will appear invisible in the video feed.

6. Press the 'q' key to quit the program.

## Customization

- If you want to use a different color for the cloak, modify the lower_bound and upper_bound values in the code. These values represent the lower and upper HSV color range for the cloak. Adjust them to match the color you want to make invisible.

- Feel free to experiment with different colors and thresholds to achieve the desired effect.

## Notes

- Ensure that the background and the object/person being covered do not have the same color, as it may affect the invisibility effect.

- For best results, use a well-lit environment and a solid-colored cloth without any patterns.

- This project is for educational purposes and may not achieve perfect invisibility. It is a fun demonstration of computer vision techniques.

## Credits

This project is inspired by the "Invisible Cloak" effect from the Harry Potter movies and is created using the OpenCV library in Python.

