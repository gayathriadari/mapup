import pandas as pd
import numpy as np
df=pd.read_csv(r'C:/Users/91630/Documents/MapUp-Data-Assessment-F-main/datasets/dataset-1.csv')
def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    
    id_1_vals=df['id_1'].unique()
    id_2_vals=df['id_2'].unique()
    car_matrix=pd.DataFrame(0,index=id_1_vals,columns=id_2_vals)
    for index,row in df.iterrows():
        car_matrix.at[row['id_1'],row['id_2']]=row['car']
    return car_matrix
r_matrix=generate_car_matrix(df)
print(r_matrix)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df['car_type'] = pd.cut(df['car'],bins=[float('-inf'), 15, 25, float('inf')],labels=['low', 'medium', 'high'],right=False)
    
    type_counts = df['car_type'].value_counts().to_dict()
    
    sorted_type_counts = dict(sorted(type_counts.items()))
    
    return sorted_type_counts
    return dict()
result = get_type_count(df)
print(result)

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    mean_bus = df['bus'].mean()
    bus_indices = np.where(df['bus'] > 2 * mean_bus)[0]
    bus_indices.sort()
    return bus_indices.tolist()
result = get_bus_indexes(df)
print(result)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    route_avg_truck = df.groupby('route')['truck'].mean()
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    sorted_selected_routes = sorted(selected_routes)
    
    return sorted_selected_routes
    return list()
result = filter_routes(df)
print(result)


def multiply_matrix(r_matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modified_df = r_matrix.copy()
    modified_df = modified_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_df = modified_df.round(1)
    
    return modified_df
modified_result_df = multiply_matrix(r_matrix)
print(modified_result_df)
