from FORM import surfactants_filter
import pandas as pd

def test_HLB_filter():
    # Define test data for HLB feature
    test_data = pd.DataFrame(
        {
            "Product": [
                "TERGITOL™ 15-S-40 Surfactant",
                "TERGITOL™ P-105 Surfactant",
                "TERGITOL™ 15-S-15 Surfactant",
                "TERGITOL™ 15-S-9 Surfactant",
            ],
            "HLB": [18, 13.4, 15.4, 13.3],  # HLB values for testing
        }
    )

    # Save test data to a CSV file
    test_data.to_csv("test_HLB_data.csv", index=False)

    # Test filtering surfactants based on HLB between 13 and 15
    filtered_surfactants = surfactants_filter("HLB", "test_HLB_data.csv", 13, 15)

    # Check that the correct surfactants are returned
    assert filtered_surfactants == [
        "TERGITOL™ P-105 Surfactant",
        "TERGITOL™ 15-S-9 Surfactant",
    ]
