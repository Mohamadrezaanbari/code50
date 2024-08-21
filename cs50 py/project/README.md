GAME OF THRONES
CS50
This was my final project for conclude the CS50 Introduction to Computer Sciense course.

CS, python, flask, flask web framework, web development, CS50
#### video demo:<https://t.me/cs50_mohamadrezaanbari>
#### Description:
This program has received the characters of the Game of Thrones movie along with their series and their height in meters and in a new file the geographical area where they are located and their height in feet.
How the Program Works?
the program utilizes the python built-in library system and import.sys.In the first step, we get a csv file with the data of 20 Game of Thrones characters, this csv file includes name, dynasty and height in meters. According to their series and height in meters, we have to convert their geographical range and height to feet and receive it in a new file.
Second, define a function for the correct number of arguments and then select to correctly identify the geographic region. Specify the correct geographic region using the character-based specification file and then define the function
a third step A function is written to convert meters to feet. For this, it is enough to multiply the height in meters by 3.28 and round the result to one decimal place. To receive the new csv file, you must write a function that receives the information of the previous two functions and then delivers it to us in a new file. For this, first open the specification file with the Dict.Reader command and get the new file with the write.writerow command.
TODO:
Download
Download the Repository through Clone Repository or Download Zip
git clone https://github.com/code50/166742410/blob/ed7ab681ebdb69e03fc43cd5f2536546b973197e/project
Installation
After download, go to cmd and navigate to the project folder directory.
cd project
Use pip to install needed libraries.

$ pip install -r requirements.txt

Usage
Run the program python script project.py with python.

python project.py

Test the program python script test_project.py with pytest.

pytest test_project.py

After successfully running the program, we will have the required specifications in a new csv file.
