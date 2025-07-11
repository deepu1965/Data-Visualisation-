"""
Data Validation Script for Visualization Showcase
Validates CSV files and checks for data integrity
"""

import csv
import os
import sys
from pathlib import Path

def validate_csv_file(filepath, expected_columns=None):
    """Validate a CSV file for basic integrity"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            
            print(f"✓ {filepath}")
            print(f"  Headers: {', '.join(headers)}")
            
            if expected_columns:
                missing = set(expected_columns) - set(headers)
                if missing:
                    print(f"  Missing columns: {', '.join(missing)}")
                else:
                    print(f"  ✓ All expected columns present")
            
            row_count = sum(1 for _ in reader)
            print(f"  Rows: {row_count}")
            
            return True
            
    except FileNotFoundError:
        print(f"✗ {filepath} - File not found")
        return False
    except csv.Error as e:
        print(f"✗ {filepath} - CSV error: {e}")
        return False
    except Exception as e:
        print(f"✗ {filepath} - Error: {e}")
        return False

def main():
    """Main validation function"""
    dep_dir = Path("dep")
    
    if not dep_dir.exists():
        print("✗ dep/ directory not found")
        sys.exit(1)
    
    print("🔍 Validating Visualization Showcase Data Files\n")
    
    # Define expected columns for each file
    validation_rules = {
        "data.csv": ["Year", "Location", "No_of_Participants", "Description"],
        "vis1_data.csv": ["breed", "entries", "attendees", "category", "day"],
        "vis2a_data.csv": ["group", "breed", "points"],
        "vis2b_data.csv": ["group", "bis", "rbis"]
    }
    
    all_valid = True
    
    for filename, expected_cols in validation_rules.items():
        filepath = dep_dir / filename
        if not validate_csv_file(filepath, expected_cols):
            all_valid = False
        print()
    
    # Check HTML files exist
    html_files = ["index.html", "vis1.html", "vis2a.html", "vis2b.html", "vis3.html"]
    
    print("Checking HTML Files:")
    for html_file in html_files:
        filepath = dep_dir / html_file
        if filepath.exists():
            print(f"✓ {html_file}")
        else:
            print(f"✗ {html_file} - Missing")
            all_valid = False
    
    print(f"\n{' All validations passed!' if all_valid else 'Some validations failed!'}")
    
    return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())
