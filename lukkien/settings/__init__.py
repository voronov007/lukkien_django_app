from .test import *

if os.getenv("ENVIRONMENT", "test").lower() == "production":
    from .production import *
