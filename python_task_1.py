#!/usr/bin/env python
# coding: utf-8

# In[35]:


#Question1: Car Matrix Generation
import pandas as pd

def generate_car_matrix(df):
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car')
    
    pivot_df = pivot_df.fillna(0)
    
    for i in pivot_df.index:
        pivot_df.at[i, i] = 0
    
    return pivot_df

df = pd.read_csv('../datasets/dataset-1.csv')

result_df = generate_car_matrix(df)

print(result_df)


# In[16]:


#question 1
import pandas as pd

def generate_car_matrix(df):
    # Use pivot_table to pivot the DataFrame
    pivot_df = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)
    
    # Set diagonal values to 0
    for i in pivot_df.index:
        pivot_df.at[i, i] = 0
    
    return pivot_df

# Read the dataset-1.csv file into a DataFrame
df = pd.read_csv('../datasets/dataset-1.csv')

# Call the function with the DataFrame
result_df = generate_car_matrix(df)

# Display the result
print(result_df)


# In[36]:


#question 2 : Car Type Count Calculation
import pandas as pd

def get_type_count(df):
    df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    type_counts = df.groupby('car_type').size().to_dict()
    
    sorted_type_counts = dict(sorted(type_counts.items()))
    
    return sorted_type_counts

df = pd.read_csv('../datasets/dataset-1.csv')

result_dict = get_type_count(df)

print(result_dict)


# In[37]:


#Question 3: Bus Count Index Retrieval
import pandas as pd

def get_bus_indexes(df):
    bus_mean = df['bus'].mean()
    
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    
    bus_indexes.sort()
    
    return bus_indexes

df = pd.read_csv('../datasets/dataset-1.csv')

result_list = get_bus_indexes(df)

print(result_list)


# In[38]:


#Question 4: Route Filtering
import pandas as pd

def filter_routes(df):
    route_avg_truck = df.groupby('route')['truck'].mean()
    
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    
    selected_routes.sort()
    
    return selected_routes

df = pd.read_csv('../datasets/dataset-1.csv')

result_list = filter_routes(df)

print(result_list)

    


# In[39]:


#Question 5: Matrix Value Modification
import pandas as pd

def multiply_matrix(input_df):
    modified_df = input_df.copy()

    modified_df = modified_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    modified_df = modified_df.round(1)

    return modified_df

df = pd.read_csv('../datasets/dataset-1.csv')

car_matrix_df = generate_car_matrix(df)

result_df = multiply_matrix(car_matrix_df)

print(result_df)


# In[ ]:




