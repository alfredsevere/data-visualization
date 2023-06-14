import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_data(file_path):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(file_path)
    return df

def plot_data(df, x, y):
    plt.figure(figsize=(10,6))
    sns.set(style="whitegrid")
    sns.barplot(x=x, y=y, data=df)
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.title('Barplot of Y vs X')
    plt.show()

if __name__ == "__main__":
    file_path = 'data.csv'  # replace with your file path
    df = load_data(file_path)

    # Assume that 'x_column' and 'y_column' are the names of the columns we are interested in
    plot_data(df, 'x_column', 'y_column')
