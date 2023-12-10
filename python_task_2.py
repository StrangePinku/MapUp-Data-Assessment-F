#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Question1: Distance Matrix Calculation
import pandas as pd
import networkx as nx

def calculate_distance_matrix(df):
    G = nx.DiGraph()

    for _, row in df.iterrows():
        G.add_edge(row['id_start'], row['id_end'], distance=row['distance'])
    
    distance_matrix = nx.floyd_warshall_numpy(G, weight='distance')

    distance_df = pd.DataFrame(distance_matrix, index=G.nodes, columns=G.nodes)

    return distance_df

df = pd.read_csv('../datasets/dataset-3.csv')

result_df = calculate_distance_matrix(df)

print(result_df)


# In[38]:


#Question2: Unroll Distance Matrix
import pandas as pd

def unroll_distance_matrix(distance_df):
    unrolled_data = []

    for id_start in distance_df.index:
        for id_end in distance_df.columns:
            if id_start == id_end:
                continue
            
            distance = distance_df.loc[id_start, id_end]

            unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

unrolled_df = unroll_distance_matrix(result_df)
print(unrolled_df)


# In[39]:


#question3: Finding IDs within Percentage Threshold
import pandas as pd

def find_ids_within_ten_percentage_threshold(unrolled_df, reference_value):
    reference_df = unrolled_df[unrolled_df['id_start'] == reference_value]
    
    reference_average = reference_df['distance'].mean()

    threshold_low = reference_average - 0.1 * reference_average
    threshold_high = reference_average + 0.1 * reference_average

    # Filter the DataFrame based on the threshold values
    within_threshold_df = unrolled_df[(unrolled_df['id_start'] != reference_value) & 
                                      (unrolled_df['distance'] >= threshold_low) &
                                      (unrolled_df['distance'] <= threshold_high)]

    result_list = sorted(within_threshold_df['id_start'].unique())

    return result_list

reference_value = '1001472.0'
result_list = find_ids_within_ten_percentage_threshold(unrolled_df, reference_value)

print(result_list)


# In[40]:


#question4: Calculate Toll Rate
def calculate_toll_rate(unrolled_df):
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = f'{vehicle_type}_toll'
        unrolled_df[column_name] = unrolled_df['distance'] * rate_coefficient

    return unrolled_df

result_df_with_toll = calculate_toll_rate(unrolled_df)

print(result_df_with_toll)


# In[ ]:




