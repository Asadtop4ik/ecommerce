from django.core.management.utils import get_random_secret_key

# Generate a new secret key
new_secret_key = get_random_secret_key()

# Print the new secret key
print(new_secret_key)
