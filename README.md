# Naukri Profile Updater - Python Web Automation

Automate the process of updating your Naukri profile with this Python script. This script uses web automation with Selenium to log in to your Naukri account and update your resume headline periodically.

## Prerequisites

Before running the script, ensure that you have the following installed on your system:

1. Python: Make sure to install Python and select the option to add it to the system path during installation.

2. Selenium: Install the Selenium library using pip with the following command:

```
pip install selenium
```

3. Webdriver Auto Update: Install the webdriver_auto_update package using pip:

```
pip install webdriver_auto_update
```

## Configuration

1. Open the script configure.py and locate the following variables:

   - `email`: Enter your Naukri account email here.
   - `password`: Enter your Naukri account password here.
   - `resume_headline`: Set the desired resume headline you want to update.

2. Set the `cooldown_time` variable:

   - `cooldown_time`: Set the frequency (in seconds) with which you want to update your Naukri profile. For example, if you want to update the profile every 1 hours, set `cooldown_time = 3600`.

3. Background Execution:

   By default, the script runs in the foreground and you can see the browser automation. If you want the script to execute in the background, set `background = True`. Note that some operating systems may have limitations for background execution.

## Running the Script

To execute the script, simply run the Python script with the following command:

```
python main.py
```

The script will now automatically log in to your Naukri account using the provided credentials, update the resume headline, and repeat this process at the specified `cooldown_time` interval.

**Important:** Please ensure that you use this script responsibly and in accordance with Naukri's terms of service. Using automation scripts may violate the platform's usage policies, so use it at your own risk.

**Note:** This script uses Selenium to automate web interactions, and it may require additional configurations based on your operating system and browser. By default, it is set up to use the Chrome web browser. Make sure you have the appropriate Chrome driver installed (compatible with your Chrome version) and available in the system path.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

If you encounter any issues or have suggestions for improvement, please feel free to create an issue or submit a pull request. Happy automating!
