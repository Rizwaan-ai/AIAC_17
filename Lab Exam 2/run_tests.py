#!/usr/bin/env python3
"""
Test runner script for both task1 and task2 test suites.
"""

import subprocess
import sys


def run_tests():
    """Run all test suites and display results."""
    print("=" * 60)
    print("RUNNING TEST SUITES")
    print("=" * 60)
    
    # Run task1 tests
    print("\n🔍 Running Task1 (Email Deduplication) Tests...")
    print("-" * 50)
    result1 = subprocess.run([sys.executable, "-m", "pytest", "test_task1.py", "-v"], 
                           capture_output=True, text=True)
    print(result1.stdout)
    if result1.stderr:
        print("STDERR:", result1.stderr)
    
    # Run task2 tests
    print("\n🔍 Running Task2 (Slugify) Tests...")
    print("-" * 50)
    result2 = subprocess.run([sys.executable, "-m", "pytest", "test_task2.py", "-v"], 
                           capture_output=True, text=True)
    print(result2.stdout)
    if result2.stderr:
        print("STDERR:", result2.stderr)
    
    # Run all tests together
    print("\n🔍 Running All Tests Together...")
    print("-" * 50)
    result_all = subprocess.run([sys.executable, "-m", "pytest", "test_task1.py", "test_task2.py", "-v"], 
                              capture_output=True, text=True)
    print(result_all.stdout)
    if result_all.stderr:
        print("STDERR:", result_all.stderr)
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Task1 Tests Exit Code: {result1.returncode}")
    print(f"Task2 Tests Exit Code: {result2.returncode}")
    print(f"All Tests Exit Code: {result_all.returncode}")
    
    if result_all.returncode == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed. Check output above for details.")


if __name__ == "__main__":
    run_tests()
