# OCR-Text-Recognition-and-Clicker-Script
![image](https://user-images.githubusercontent.com/107073565/230533576-e0615cdd-bde9-4cc9-a2ba-4f9de5236ca5.png)

This Python script uses Tesseract OCR to extract text from a specific area of the screen and clicks on a designated position depending on the extracted text. This script is designed to automate clicking actions based on specific text patterns.

## Getting Started -
### Prerequisites:
Before using this script, you need to have Python 3 installed on your computer. Additionally, you need to install the following packages:

* ```pyautogui```: used for automating mouse clicks
* ```pytesseract```: used for OCR text recognition
* ```keyboard```: used for detecting keyboard inputs
* ```Pillow```: used for image processing
* The appropriate Tesseract OCT for your OS

#### You can install the python packages using pip:

```python
pip install pyautogui pytesseract keyboard Pillow
```

#### Install Tesseract OCR:

##### * This script is designed to work with **Windows**: You can download the installer from the Tesseract GitHub page (https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions. Please install in the default directory



## Installation -
To use this script, download or clone this repository to your computer.

## Usage -

### Configuration:
Before running the script, you need to configure it to match your specific needs.

To configure the script, open the ```click.py``` file and edit the values in the **START CONFIG** section:

* ```left```: the left-to-right (horizontal) position in px of the area you want text read from
* ```top```: the top-to-bottom (vertical) position in px of the area you want text read from
* ```width```: the width of the area you want text read from
* ```height```: the height of the area you want text read from
* ```text1```: the first text pattern to search for
* ```text2```: the second text pattern to search for
* ```click_pos1```: the position to click if text1 is found
* ```click_pos2```: the position to click if text2 is found
* ```toggle_key```: the keyboard key to turn the script on/off
* ```wait_time```: the delay before clicking

### Running the Script:
To run the script, open the command prompt or terminal, navigate to the directory where the click.py file is located, and run the command:
```python click.py```

The script will initialize and wait for you to press the toggle_key to start. 

![image](https://user-images.githubusercontent.com/107073565/230533457-6eec96fd-d8f3-45cd-b8b5-884b2de42942.png)

Once the script is running, it will continuously search for the specified text patterns in the specified area of the screen every so seconds that you set in the config (Default 5, I reccomend not going under 2 or 3 as it will get hard to stop the script). If the script detects the text, it will click on the designated position.

![image](https://user-images.githubusercontent.com/107073565/230533844-c2671f16-ffd4-4e99-a871-227cf869fc34.png)
![image](https://user-images.githubusercontent.com/107073565/230533576-e0615cdd-bde9-4cc9-a2ba-4f9de5236ca5.png)
![image](https://user-images.githubusercontent.com/107073565/230533863-3b58807e-49b4-4762-956f-8d8fd7a8afce.png)
![image](https://user-images.githubusercontent.com/107073565/230533985-984ec2ec-bad4-49e4-bd60-2849126ec74c.png)



To stop the script, press the toggle_key again, or press ctrl+c at anytime.

## Authors -
Kawaii - Initial work

## Acknowledgments -
* [PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/index.html)
* [pytesseract documentation](https://pypi.org/project/pytesseract/)
* [keyboard documentation](https://github.com/boppreh/keyboard)
* [Pillow documentation](https://pillow.readthedocs.io/en/stable/)



