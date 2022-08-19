# Noted
A simple todo app made in django

## Features:
- User Authentication - Users can register, login and logout
- Add, Edit, Mark tasks as Complete and Delete Tasks

## Screenshots of the application
![screen1](https://user-images.githubusercontent.com/79845962/185420072-68505552-6b76-4dfe-8946-81173b24d9aa.png)
![screen2](https://user-images.githubusercontent.com/79845962/185420077-de1f880c-afea-4007-a7e5-5263eb3b2a15.png)
![screen3](https://user-images.githubusercontent.com/79845962/185420082-b1dd1d19-93bd-4818-9924-405b73b39a27.png)
![screen4](https://user-images.githubusercontent.com/79845962/185420085-8cd9bb4a-ef90-4d5d-9e03-519ee8edea50.png)
![screen5](https://user-images.githubusercontent.com/79845962/185420089-a2088482-effc-4c1c-921e-2b78f834be3f.png)
![screen6](https://user-images.githubusercontent.com/79845962/185420092-899a096f-ed59-47b7-97bd-f0a1d690688e.png)

## Setup (Windows)
0. Install virtual enviroment.
```bash
pip install virtualenv
```

1. Open cmd and change your directory to Desktop ("cd Desktop").

2. Now it's time to create your virtual enviroment using this command:
```bash
virtualenv "name"
```
- Change the "name" to whatever you want (eg. ToDoApp)

3. You need to activate your virtual enviroment, to do this go to created directory and execute command below:
```bash
Scripts\activate
```
4. To get this repository, run the following command inside your git enabled terminal:
```bash
git clone https://github.com/dawdom34/Noted.git
```
 
5. Go to Noted repository and execute this command:
```bash
pip install -r requirements.txt
```
- This command will install all necessary packages (including django) to start the project in an isolated environment

6. Create all the migrations file (database migrations) required to run this App by running the fallowing command inside Noted directory:
```bash
python manage.py makemigrations todolist
```

7. Now, to apply this migrations run the following command:
```bash
python manage.py migrate
```

8. Now create admin user. Execute this command and follow the instructions: 
```bash
python manage.py createsuperuser
```

9. Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command:
```bash
python manage.py runserver
```
- Once the server is hosted, head over to http://127.0.0.1:8000/
