DRF View Types : 

main 3 : 

1. APIView

When i need fine-grained control over request handling or complext buiseness logic

 we manually write all get , post, delete() 

 2. Generic Views 
Mostly used in industry: 
Prebuild logic 
ListAPIView --> Get List 
CreateAPIView--> 
RetrieveAPIView 

I prefer Generic view for standard CRUD  operations because they reduce boilerplate and improve readability 


3. viewSets (Most Scalable / Enterprise Style)

for scalable APIs, I use viewsets with routers to keep routing and logic clean.

# Event Reservation API

Django REST API for managing events and seat reservations with validation to prevent overbooking.

---

## Project Notes

- Migrations are committed inside `events/migrations/`
- Postman screenshots are available in the `screenshots/` directory

---

##  How to Run the Project

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

python -m venv venv
venv\Scripts\activate   # (Windows)

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver