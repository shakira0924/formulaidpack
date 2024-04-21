from FORM import surfactants_filter
import pandas as pd

def test_cloud_point_filter():
    # Define test data for Cloud Point feature.
    test_data = pd.DataFrame({"Product": ["ECOSURF™ EH-3 Surfactant", 
                                          "TERGITOL™ L-81 Surfactant", 
                                          "TERGITOL™ 15-S-40 (70%) Surfactant", 
                                          "TRITON™ X-15", 
                                          "TRITON™ X-100"],
                              "Cloud Point": ["Disp", 20, ">100", "Ins", 66]})

    # Convert special cases to float('inf').
    test_data["Cloud Point"] = test_data["Cloud Point"].replace({"Disp": float("inf"), ">100": float("inf")})

    # Save test data to a CSV file.
    test_data.to_csv("test_cloud_point_data.csv", index = False)

    # Test filtering surfactants based on Cloud Point.
    filtered_surfactants = surfactants_filter("Cloud Point", "test_cloud_point_data.csv", 25)

    # Check that the correct surfactants are returned.
    assert filtered_surfactants == ["ECOSURF™ EH-3 Surfactant", "TERGITOL™ 15-S-40 (70%) Surfactant", "TRITON™ X-100",]