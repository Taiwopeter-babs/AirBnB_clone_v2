#!/usr/bin/python3
import os

print("TEST_ENV" in os.environ)
if os.getenv("TEST_ENV") == "test_db":
    print("Test_db")
elif os.getenv("TEST_ENV") == "dev_db":
    print("Dev_db")
