# from django.contrib.auth.models import Group, User, Permission
# from django.contrib.contenttypes.models import ContentType
# from .models import User
# from armsApp.models import Reservation, Airlines, Airport, Flights

# # Define groups
# group_admin, created = Group.objects.get_or_create(name='Admin')
# group_staff, created = Group.objects.get_or_create(name='Staff')
# group_normal, created = Group.objects.get_or_create(name='Normal')

# # Define permissions for each model
# airline_content_type = ContentType.objects.get_for_model(Airlines)
# airline_permissions = Permission.objects.filter(content_type=airline_content_type)

# airport_content_type = ContentType.objects.get_for_model(Airport)
# airport_permissions = Permission.objects.filter(content_type=airport_content_type)

# flight_content_type = ContentType.objects.get_for_model(Flights)
# flight_permissions = Permission.objects.filter(content_type=flight_content_type)

# reservation_content_type = ContentType.objects.get_for_model(Reservation)
# reservation_permissions = Permission.objects.filter(content_type=reservation_content_type)

# # Assign permissions to groups
# group_admin.permissions.set(airline_permissions | airport_permissions | flight_permissions | reservation_permissions)

# group_staff.permissions.set(airline_permissions | airport_permissions)

# group_normal.permissions.set(flight_permissions | reservation_permissions)

# # Retrieve user objects
# user1 = User.objects.get(username='Admin')
# user2 = User.objects.get(username='Ahmed')
# user3 = User.objects.get(username='Omar')

# # Add the user to the groups
# group_admin.user_set.add(user1)
# group_staff.user_set.add(user2)
# group_normal.user_set.add(user3)
