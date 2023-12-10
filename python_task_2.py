import pandas as pd

df=pd.read_csv(r'C:/Users/91630/Documents/MapUp-Data-Assessment-F-main/datasets/dataset-3.csv')
def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    id_list = pd.concat([df['id_start'], df['id_end']]).unique()
    distance_matrix = pd.DataFrame(index=id_list, columns=id_list)
    distance_matrix.values[[range(len(id_list))]*2] = 0
    
    for index, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[id_start, id_end] = distance
        distance_matrix.at[id_end, id_start] = distance 
    
    
    for i in id_list:
        for j in id_list:
            for k in id_list:
                if distance_matrix.at[i, j] > 0 and distance_matrix.at[j, k] > 0:
                    distance_matrix.at[i, k] = distance_matrix.at[i, j] + distance_matrix.at[j, k]

    return distance_matrix
result = calculate_distance_matrix(df)
print(result)


def unroll_distance_matrix(distance_matrix)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    
    combinations = [(i, j) for i in distance_matrix.index for j in distance_matrix.columns if i != j]
    unrolled_df = pd.DataFrame(combinations, columns=['id_start', 'id_end'])
    
    unrolled_df['distance'] = unrolled_df.apply(lambda row: distance_matrix.at[row['id_start'], row['id_end']], axis=1)
    
    return unrolled_df
result1 = unroll_distance_matrix(result)
print(result1)

def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
