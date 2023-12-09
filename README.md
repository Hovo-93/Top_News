## Scraping for News

Stack:Python,Django,BeautifulSoup,Docker

[Docker Desktop](https://www.docker.com/products/docker-desktop)for Mac or Windows [Docker Compose](https://docs.docker.com/compose) will be installed automatically. In Linux, make sure you have the latest version of  [Compose](https://docs.docker.com/compose/install/). You can also use the official  [инструкцией](https://docs.docker.com/engine/install/).

#### Step 1. Clone the repository to your computer
Enter the command:
```bash
git clone https://github.com/Hovo-93/Top_News.git
```
#### Step 2. Create a .env file in the cloned directory top_news_scraper, you can use this data
Пример:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=stripetest
DB_USER=postgres
DB_PASSWORD=zhenya
DB_HOST=db
DB_PORT=5432
```
Run  Docker 
#### To rebuild and run containers
```bash
    docker-compose up --build -d 

```
#### To create a superuser
```bash
    1 docker  ps 
    2 docker-compose run web_app python manage.py createsuperuser
```
Run locally

#### Step 1. To create and activate a virtual environment:
```python
    python -m venv venv

    venv\Scripts\activate - для Windows;
    
    source venv/bin/activate - для Linux и MacOS
```
#### Step 2. Create and apply migrations:
```python
    python manage.py makemigrations
    python manage.py migrate
```
#### Step 3. Install all dependencies:
```python
    pip install -r requirements.txt
```
#### Step 4. Create a superuser:
```json
    python manage.py createsuperuser
```
#### Шаг 5.Admin Panel:
```json
    http://127.0.0.1:8000/admin/
```
#### Step 6. Run the server locally:
```python
    python manage.py runserver
```

You should click 1.Link 2.Update Latest News 3.Top news  


Server Link: http://89.104.68.24:8080/ 