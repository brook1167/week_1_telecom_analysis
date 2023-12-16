import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import seaborn as sns
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px

def app():

    st.title("Telecommunication User Over View Analysis")
    df_over_view = pd.read_csv('data/telecom_clean_data.csv')

    st.header("Top 10 handsets used by the customers")
    st.bar_chart(df_over_view['Handset Type'].value_counts()[0:10])

    st.header("Top 3 handset manufacturers")
    st.bar_chart(df_over_view['Handset Manufacturer'].value_counts()[0:3])

    st.header("Top 5 handsets per top 3 handset manufacturer")
    


    top_apple = df_over_view.loc[df_over_view['Handset Manufacturer'] == 'Apple']

    top_apple = df_over_view.loc[df_over_view['Handset Manufacturer'] == 'Apple']

# Group by Handset Manufacturer and Handset Type, then count occurrences
    top_apple = top_apple.groupby(['Handset Manufacturer', 'Handset Type']).agg({'Handset Type': ['count']})
    top_apple.columns = ['count']

# Select the top 5 Apple handsets
    top_apple = top_apple.nlargest(5, 'count')


# Plot the bar chart using Matplotlib and display it in the Streamlit app
    fig, ax = plt.subplots()
    top_apple.plot.bar(y='count', ax=ax, stacked=True, color='#ec2123')
    ax.set_title("Top 5 Apple Handsets")
    ax.set_xlabel("Handset Type")
    ax.set_ylabel("Count")

# Display the plot in the Streamlit app
    st.pyplot(fig)

    st.header('Top 5 Samsung Handsets')

    top_samsung = df_over_view.loc[df_over_view['Handset Manufacturer'] == 'Samsung']
    top_samsung = top_samsung.groupby(['Handset Manufacturer', 'Handset Type']).agg({'Handset Type': ['count']})
    top_samsung.columns = ['count']
    top_samsung = top_samsung.nlargest(5, 'count')

# Plot using Matplotlib
    fig, ax = plt.subplots()
    top_samsung.plot.bar(y='count', ax=ax, stacked=True, color='#ffc206')
    plt.xlabel("Handset Type")
    plt.ylabel("Count")
    st.pyplot(fig)



    st.header('Top 5 Huawei Handsets')

# Filter Huawei data
    top_huawei = df_over_view.loc[df_over_view['Handset Manufacturer'] == 'Huawei']

# Group by Manufacturer and Type, and aggregate the count
    top_huawei = top_huawei.groupby(['Handset Manufacturer', 'Handset Type']).size().reset_index(name='count')

# Get the top 5 handsets
    top_huawei = top_huawei.nlargest(5, 'count')

# Create a Streamlit app


# Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(top_huawei['Handset Type'], top_huawei['count'], color='#3d85c6')
    ax.set_title("Top 5 Huawei Handsets")
    ax.set_xlabel("Handset Type")
    ax.set_ylabel("Count")

# Display the plot in Streamlit
    st.pyplot(fig)

    # remove warning 

    st.set_option('deprecation.showPyplotGlobalUse', False)


    st.title('number of xDR sessions')

# Plot Distrubution
    column_to_plot = 'Dur. (ms).1' 
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()


    st.header('Total Upload')


    column_to_plot = 'Total UL (Bytes)' 
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()



    st.header('Total Downloads Bytes')

    column_to_plot = 'Total DL (Bytes)' 
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()


    st.header('Social Media Total Upload and Download Data')

    column_to_plot = 'Social_Media_Total_Data' 
    df_over_view['Social_Media_Total_Data'] = df_over_view['Social Media DL (Bytes)'] + df_over_view['Social Media UL (Bytes)']
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()


    st.header('Google Total Data')

    column_to_plot = 'Google_Total_Data' 
    df_over_view['Google_Total_Data'] = df_over_view['Google DL (Bytes)'] + df_over_view['Google UL (Bytes)']
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()

    st.header('Total Email Data')

    column_to_plot = 'Email_Total_Data' 
    df_over_view['Email_Total_Data'] = df_over_view['Email DL (Bytes)'] + df_over_view['Email UL (Bytes)']
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()



    st.header('Total Youtube Data')

    column_to_plot = 'Youtube_Total_Data' 
    df_over_view['Youtube_Total_Data'] = df_over_view['Youtube DL (Bytes)'] + df_over_view['Youtube UL (Bytes)']
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()


    st.header('Total Netflix Data')

    column_to_plot = 'Netflix_Total_Data' 
    df_over_view['Netflix_Total_Data'] = df_over_view['Netflix DL (Bytes)'] + df_over_view['Netflix UL (Bytes)']
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()



    st.header('Total Gaming Data')

    column_to_plot = 'Gaming_Total_Data' 
    df_over_view['Gaming_Total_Data'] = df_over_view['Gaming DL (Bytes)'] + df_over_view['Gaming UL (Bytes)']
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()

    st.header('Other Total Data')

    column_to_plot = 'Other_Total_Data' 
    df_over_view["Other_Total_Data"]=df_over_view["Other DL (Bytes)"]+df_over_view["Other UL (Bytes)"]
    plt.figure(figsize=(8, 6))
    sns.histplot(df_over_view[column_to_plot], color='dodgerblue', kde=True)
    plt.title(f'Distrubution of {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()
    



  # scatter plot for TotalData vs Gaming Data usage

    st.header('Total Data Vs Gaming Data Usage')

    x_column = df_over_view["Gaming_Total_Data"]=df_over_view["Gaming DL (Bytes)"]+df_over_view["Gaming UL (Bytes)"]
    y_column = df_over_view["Total UL and DL"]=df_over_view["Total UL (Bytes)"]+df_over_view["Total DL (Bytes)"]


    st.scatter_chart(df_over_view[['Gaming_Total_Data', 'Total UL and DL']].sample(1000))


    st.header('Total Data Vs Youtube Total Data')

    x_column = df_over_view["Youtube_Total_Data"]=df_over_view["Youtube DL (Bytes)"]+df_over_view["Youtube UL (Bytes)"]
    y_column = df_over_view["Total UL and DL"]=df_over_view["Total UL (Bytes)"]+df_over_view["Total DL (Bytes)"]


    st.scatter_chart(df_over_view[['Youtube_Total_Data', 'Total UL and DL']].sample(1000))




    st.header('Total Data Vs Email Total Data')

    x_column = df_over_view["Email_Total_Data"]=df_over_view["Email DL (Bytes)"]+df_over_view["Email UL (Bytes)"]
    y_column = df_over_view["Total UL and DL"]=df_over_view["Total UL (Bytes)"]+df_over_view["Total DL (Bytes)"]


    st.scatter_chart(df_over_view[['Email_Total_Data', 'Total UL and DL']].sample(1000))

    st.header('Total Data Vs Social Media Total Data')

    x_column = df_over_view["Social_Media_Total_Data"]=df_over_view["Social Media DL (Bytes)"]+df_over_view["Social Media UL (Bytes)"]
    y_column = df_over_view["Total UL and DL"]=df_over_view["Total UL (Bytes)"]+df_over_view["Total DL (Bytes)"]


    st.scatter_chart(df_over_view[['Social_Media_Total_Data', 'Total UL and DL']].sample(1000))


    st.header('Total Data Vs Netflix Data')

    x_column = df_over_view["Netflix_Total_Data"]=df_over_view["Netflix DL (Bytes)"]+df_over_view["Netflix UL (Bytes)"]
    y_column = df_over_view["Total UL and DL"]=df_over_view["Total UL (Bytes)"]+df_over_view["Total DL (Bytes)"]


    st.scatter_chart(df_over_view[['Netflix_Total_Data', 'Total UL and DL']].sample(1000))


    st.header('Total Data Vs Other_Total_Data')

    x_column = df_over_view['Other_Total_Data'] = df_over_view["Other DL (Bytes)"] + df_over_view['Other UL (Bytes)']
    y_column = df_over_view["Total UL and DL"]=df_over_view["Total UL (Bytes)"]+df_over_view["Total DL (Bytes)"]


    st.scatter_chart(df_over_view[['Other_Total_Data', 'Total UL and DL']].sample(1000))



    columns = ['Youtube_Total_Data', 'Google_Total_Data', 'Email_Total_Data','Social_Media_Total_Data', 'Netflix_Total_Data', 'Gaming_Total_Data', 'Other_Total_Data', 'Total UL and DL']
    corr = df_over_view[columns].corr()
    
    st.title("Correlation of Usage of User Data Volume")

# Display correlation matrix as text
    st.write("Correlation Matrix:")
    st.write(corr)