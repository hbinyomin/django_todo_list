# To-Do App

A simple to-do app that supports tasks associated with an individual user. 
Each task includes a field that can store string, number, or boolean values, based on user's choice.

 
## Setup Instructions

**Clone the Repository**

```
git clone https://github.com/hbinyomin/django_todo_list.git
cd django_todo_list
```


**Create Virtual Environment**

```
python -m venv venv
source venv/bin/activate    # (for Linux)
venv\Scripts\activate       # (for Windows)
```

**Install Dependencies**

```
pip install -r requirements.txt
```

**Apply Migrations**

```
python manage.py migrate
```

**Seed DB**

- This command assumes that you have no existing users with username 'ruvain' or 'chaim'
```
python manage.py populate_db
```


**Run the Development Server**

```
python manage.py runserver
```

**Open in Browser**

http://127.0.0.1:8000/login

**Login**

- You have one username '**ruvain**' and a second  username '**chaim**'
- the password for both is '**go**'


