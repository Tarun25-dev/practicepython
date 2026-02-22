# os.environ → A dictionary-like object containing all environment variables.

# os.environ.get(key) → Safely returns the value of the environment variable key.

# Returns None if the variable does not exist.

import os 
path_value = os.environ.get("PATH")
print("Path value is: ",path_value) # it gives all the paths from path key