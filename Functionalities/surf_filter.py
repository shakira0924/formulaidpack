def surfactants_filter(feature, min_value, df_path:str, max_value=None):
    """
    Filter surfactants based on the specified feature and range.

    Parameters:
        feature (str): The feature (column) to filter by.
        min_value (float): The minimum value of the range.
        max_value (float or None): The maximum value of the range. Default is None.

    Returns:
        list: A list of surfactant names that meet the criteria.
    """
    surfactants_df = pd.read(df_path)
    try:
        if max_value is not None:
            # Filter surfactants based on the specified feature and range
            surfactants = surfactants_df[
                (surfactants_df[feature] >= min_value) &
                (surfactants_df[feature] <= max_value)
            ]
        else:
            # Filter surfactants based on the specified feature and minimum value only
            surfactants = surfactants_df[
                (surfactants_df[feature] >= min_value)
            ]

        # Handle special cases where value is 'Disp' or '>100'
        surfactants = surfactants.replace({'Disp': float('inf'), '>100': float('inf')})

        # Extract names of surfactants from the "Product" column
        surfactant_names = surfactants['Product'].tolist()
        return surfactant_names
    
    except KeyError:
        print(f"Error: '{feature}' is not a valid feature.")
        return []
