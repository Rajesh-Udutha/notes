import pandas as pd
import xport  # Assuming your custom module is accessible
import xport.v56
import os

with open('CTST002A1001.xpt', 'rb') as f:
    dataset = xport.v56.load(f)
    print(dir(dataset))
    dataframes = dataset.values()  # Assuming it returns a list of DataFrames

    for i, df in enumerate(dataframes):
        dataset_name = list(dataset.keys())[i].replace('.DAT','')  # Extract dataset name
        print(dataset_name)
        output_file = "XPT_CSV/"+f"{dataset_name}.xpt"
        print(output_file)


        with open(output_file, 'wb') as f_out:  # Open in binary write mode
            xport.v56.dump(df, f_out)

