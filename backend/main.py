from inspira import Inspira
from inspira.middlewares.cors import CORSMiddleware

origins = ["http://localhost:5173"]

app = Inspira(secret_key="SM3XuO4DOdk0PG5a_Qt4wkHZtKxbaA2yUxjPxJZ18nkBHFAULd")

cors = CORSMiddleware(origins)
app.add_middleware(cors)