# app.py
import logging

# Configure root logging
logging.basicConfig(
    level=logging.INFO,  # default level (can be overridden by pytest.ini or CLI)
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)

def add(a, b):
    result = a + b
    # Debug-level log (won't show unless level is set to DEBUG)
    logger.debug("add() inputs: a=%s, b=%s", a, b)
    # Info-level log (shows by default)
    logger.info("add() result=%s", result)
    return result

if __name__ == "__main__":
    print("Running app.py directly...")
    add(2, 3)
    add(-5, 7)
