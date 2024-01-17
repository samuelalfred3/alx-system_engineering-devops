* Command line for the win

* Background Context
CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

* General
A README.md file, at the root of the folder of the project, is mandatory
This project will be manually reviewed.
As each task is completed, the name of that task will turn green
Create a screenshot, showing that you completed the required levels
Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

* References :

SFTP Guide
SFTP File Transfer Tutorial

* Here are the steps to follow:

Take the screenshots of the completed levels as mentioned in the general requirements.
Open a terminal or command prompt on your local machine.
Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
Once connected, navigate to the directory where you want to upload the screenshots.
Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.
* NOTE :
The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/

Steps you followed to use the SFTP command-line tool.
-Connect to the Sandbox Environment:
-Open a terminal on the local machine.
-Use the sftp command to connect to the sandbox environment.
sftp <username>@<hostname>
-Navigate to the Directory for Upload:
-Move to the directory on the sandbox environment where screenshots will be uploaded.
cd /root/alx-system_engineering-devops/command_line_for_the_win/
-Upload Screenshots Using put Command:
-Use the put command to upload each screenshot.
Replace <local_screenshot> with the actual filename of the screenshot.
put <local_screenshot>
-Ensure that all screenshots are successfully transferred to the sandbox environment by checking the contents of the remote directory.
sftp> ls
-Once all screenshots are uploaded, proceed to push the changes to GitHub.
