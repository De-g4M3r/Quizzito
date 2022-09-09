from random import shuffle, randrange
import string
from django.urls import path
from .views import (
    score,
    homepage,
    database,
    questions_generator,
    qg_algorithm,
    q_delete,
    update,
    update_algorithm,
    from_database_to_homepage_redirector,
    back_to_database, 
    admin_login_verification,
)


d = list(
    string.ascii_letters+string.digits
)
shuffle(d)
DATABASE_URL = "".join(d)


urlpatterns = [
    path("", homepage, name='home'),
    path("score/", score, name='scoring'),
    path("admin_login/", admin_login_verification, name='adminlogin'),
    path(f"{DATABASE_URL}/", database, name='database'),
    path(f"{DATABASE_URL}/back_to_homepage/", from_database_to_homepage_redirector, name='database_home'),
    path(f"{DATABASE_URL}/add/", questions_generator, name='questions_generator'),
    path(f"{DATABASE_URL}/add/generated/", qg_algorithm, name='questions_generator_algorithm'),
    path(f"{DATABASE_URL}/add/back_to_database/", back_to_database, name='back_to_database'),
    path(f"{DATABASE_URL}/delete/<int:q_id>", q_delete, name="delete"),
    path(f"{DATABASE_URL}/update/<int:q_id>", update, name="update"),
    path(f"{DATABASE_URL}/update/back_to_database/", back_to_database, name='back_to_database'),
    path(f"{DATABASE_URL}/update/updated/<int:q_id>", update_algorithm, name='update_algorithm')
]
