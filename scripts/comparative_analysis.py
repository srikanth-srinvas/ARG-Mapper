import pandas as pd
import os

def load_arg_results(arg_dir):
    arg_files = [f for f in os.listdir(arg_dir) if f.endswith('_args.txt')]
    arg_data = []
    for arg_file in arg_files:
        file_path = os.path.join(arg_dir, arg_file)
        sample_name = arg_file.replace('_args.txt', '')
        df = pd.read_csv(file_path, sep='\t')
        df['Sample'] = sample_name
        arg_data.append(df)
    return pd.concat(arg_data, ignore_index=True)

def compare_args(arg_data):
    summary = arg_data.groupby(['Sample', 'Resistance gene']).size().unstack(fill_value=0)
    return summary
