from config import get_env_setup

# Get all environment variables
env_vars = get_env_setup.get_var()
print(env_vars['database'])

# Or use the module-level variables
import config
print(config.database)
