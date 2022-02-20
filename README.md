# test_app
Trip

Running the app:

docker-compose build
docker-compose up

docker exec -it d8119ea8af8f python manage.py makemigrations
docker exec -it d8119ea8af8f python manage.py migrate

docker exec -it d8119ea8af8f python manage.py createsuperuser

server runs on 0.0.0.0:8000

routs:

admin/
api-auth/
user-list/ [name='user_list']
user-create/ [name='user_create']
user-details/<int:id>/ [name='user_detail']
user-change/<int:id>/ [name='change_user']
user-delete/<int:id>/ [name='delete_user']
destination-list/ [name='destination_list']
destination-create/ [name='destination_create']
destination-details/<int:id_destination>/ [name='destination_details']
destination-change/<int:id_destination>/ [name='destination_change']
destination-delete/<int:id_destination>/ [name='destination_delete']
(start route)[name='trip_list']
trip-create/ [name='trip_create']
trip-details/<int:id_trip>/ [name='trip_details']
trip-change/<int:id_trip>/ [name='trip_change']
trip-delete/<int:id_trip>/ [name='trip_delete']