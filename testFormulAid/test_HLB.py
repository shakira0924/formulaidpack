import surf_filter
import pandas as pd

# Load the .csv file into a pandas DataFrame for testing
test_data = pd.DataFrame({
    'Product': ['TERGITOL™ 15-S-40 Surfactant', 'TERGITOL™ P-105 Surfactant', 'TERGITOL™ 15-S-15 Surfactant', 'TERGITOL™ 15-S-9 Surfactant'],
    'HLB': [18, 13.4, 15.4, 13.3]  # HLB values for testing
})

def surfactants_filter():
    # Override the surfactants_df variable with test data
    surfactants_filter.surfactants_df = test_data
    
    # Test filtering surfactants based on HLB between 13 and 15
    filtered_surfactants = surfactants_filter.filter_surfactants_by_range('HLB', 13, 15)
    
    # Check that the correct surfactants are returned
    assert filtered_surfactants == ['TERGITOL™ P-105 Surfactant', 'TERGITOL™ 15-S-9 Surfactant']