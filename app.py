# app.py
import logging

# Configure logging once, at module import or __main__ execution
logging.basicConfig(
    level=logging.INFO,  # change to DEBUG for more detail
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)

def add(a, b):
    result = a + b
    logger.info("add() called with a=%s, b=%s, result=%s", a, b, result)
    return result

if __name__ == "__main__":
    print("Running app.py directly...")
    add(2, 3)
    add(-5, 7)
