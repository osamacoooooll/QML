
import numpy as np
import pandas as pd
# def load_data(data_file,N,validation_pts):
#     dataset = np.loadtxt('./data/{}.csv'.format(data_file), delimiter=',')

#     data = dataset[:N+validation_pts, :-1]
#     t = dataset[:N + validation_pts, -1]

#     return data,t

def load_data(data_file,N,validation_pts):

         # Replace with your actual file name without .csv extension
        
        # Load the CSV file using pandas
        df = pd.read_csv('./data/{}.csv'.format(data_file))

        # Convert the DataFrame to a numpy array
        dataset = df.values
        data = dataset[:N+validation_pts, :-1]
        t = dataset[:N + validation_pts, -1]

        return data,t