import surf_filter
import pandas as pd

def test_cloud_point_filter():
    # Define test data for Cloud Point feature
    test_data = pd.DataFrame({
        'Product': ['ECOSURF™ EH-3 Surfactant', 'TERGITOL™ L-81 Surfactant', 'TERGITOL™ 15-S-40 (70%) Surfactant', 'TRITON™ X-15', 'TRITON™ X-100'],
        'Cloud Point': ['Disp', 20, '>100', 'Ins', 66]
    })

    # Override the surfactants_df variable with test data
    surf_filter.surfactants_df = test_data

    # Test filtering surfactants based on Cloud Point
    filtered_surfactants = surf_filter.surfactants_filter('Cloud Point', 25)

    # Check that the correct surfactants are returned
    assert filtered_surfactants == ['ECOSURF™ EH-3 Surfactant', 'TERGITOL™ 15-S-40 (70%) Surfactant', 'TRITON™ X-100']