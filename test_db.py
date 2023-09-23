#!/usr/bin/python3

import MySQLdb

def test_create_state():
    # Replace with your own database credentials
    db = MySQLdb.connect(host="localhost", user="hb_tst", passwd="hb_pwd", db="test_db")

    try:
        cursor = db.cursor()

        # Get the initial state count
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_state_count = cursor.fetchone()[0]

        # Execute the action: Insert a new state
        cursor.execute("INSERT INTO states (name) VALUES ('California')")

        # Get the final state count
        cursor.execute("SELECT COUNT(*) FROM states")
        final_state_count = cursor.fetchone()[0]

        # Calculate the difference
        difference = final_state_count - initial_state_count

        # Assert the result
        assert difference == 1, "Test failed: State count didn't increase by 1"

        print("Test passed: State count increased by 1")

    except Exception as e:
        print(f"Test failed: {str(e)}")
    finally:
        # Close the database connection
        db.close()

# Run the test
if __name__ == "__main__":
    test_create_state()
