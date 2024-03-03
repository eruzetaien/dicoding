import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Selamat datang di Proyek Akhir!")
    st.write("Belajar Analisis Data dengan Python.")

    bike_day_df = pd.read_csv("day.csv")
    bike_hour_df = pd.read_csv("hour.csv")

    tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2",])
    
    with tab1:
        st.header("Pertanyaan 1")
        st.subheader("Apakah ada hubungan antara suhu dan kelembaban udara  dengan tingkat peminjaman sepeda?")

        fig = plt.figure(figsize=(10, 5))
        sns.regplot(x=bike_hour_df['temp'], y=bike_hour_df['cnt'], scatter_kws={'s': 50}, line_kws={'color': 'red'})
        plt.xlabel('Suhu')
        plt.ylabel('Total Peminjaman Sepeda')
        plt.title('Korelasi antara Suhu dengan Peminjaman Sepeda dalam sehari')

        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 5))
        sns.regplot(x=bike_hour_df['hum'], y=bike_hour_df['cnt'], scatter_kws={'s': 50}, line_kws={'color': 'red'})
        plt.xlabel('Kelemababan')
        plt.ylabel('Total Peminjaman Sepeda')
        plt.title('Korelasi antara Kelembaban dengan Peminjaman Sepeda dalam sehari')

        st.pyplot(fig)
    
    with tab2:
        st.header("Pertanyaan 2")
        st.subheader("Bisakah kita mengelompokkan data peminjaman sepeda berdasarkan jenis pengguna?")

        season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

        bike_day_df_copy = bike_day_df.copy()
        bike_day_df_copy['season'] = bike_day_df_copy['season'].map(season_mapping)

        result_df = bike_day_df_copy.groupby(by="season").agg({
            "casual":  lambda x: (x.sum() / bike_day_df_copy['casual'].sum()) * 100, 
            "registered": lambda x: (x.sum() / bike_day_df_copy['registered'].sum()) * 100, 
            "cnt": lambda x: (x.sum() / bike_day_df_copy['cnt'].sum()) * 100
            })

        labels = result_df.index.astype(str)

        fig = plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.pie(result_df['casual'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Casual Users by Season')
        plt.axis('equal')  

        plt.subplot(1, 3, 2)
        plt.pie(result_df['registered'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('registered Users by Season')
        plt.axis('equal')  

        plt.subplot(1, 3, 3)
        plt.pie(result_df['cnt'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('total Users by Season')
        plt.axis('equal')  

        st.pyplot(fig)


        holiday_mapping = {0: 'no', 1: 'yes'}

        bike_day_df_copy = bike_day_df.copy()
        bike_day_df_copy['holiday'] = bike_day_df_copy['holiday'].map(holiday_mapping)


        result_df = bike_day_df_copy.groupby(by="holiday").agg({
            "casual":  lambda x: (x.sum() / bike_day_df_copy['casual'].sum()) * 100, 
            "registered": lambda x: (x.sum() / bike_day_df_copy['registered'].sum()) * 100, 
            "cnt": lambda x: (x.sum() / bike_day_df_copy['cnt'].sum()) * 100
            })

        labels = result_df.index.astype(str)

        fig = plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.pie(result_df['casual'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Casual Users by holiday')
        plt.axis('equal')  

        plt.subplot(1, 3, 2)
        plt.pie(result_df['registered'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('registered Users by holiday')
        plt.axis('equal')  

        plt.subplot(1, 3, 3)
        plt.pie(result_df['cnt'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('total Users by holiday')
        plt.axis('equal')  
        
        st.pyplot(fig)


        
        weekday_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

        bike_day_df_copy = bike_day_df.copy()
        bike_day_df_copy['weekday'] = bike_day_df_copy['weekday'].map(weekday_mapping)


        result_df = bike_day_df_copy.groupby(by="weekday").agg({
            "casual":  lambda x: (x.sum() / bike_day_df_copy['casual'].sum()) * 100, 
            "registered": lambda x: (x.sum() / bike_day_df_copy['registered'].sum()) * 100, 
            "cnt": lambda x: (x.sum() / bike_day_df_copy['cnt'].sum()) * 100
            })

        labels = result_df.index.astype(str)

        fig = plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.pie(result_df['casual'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Casual Users by weekday')
        plt.axis('equal')  

        plt.subplot(1, 3, 2)
        plt.pie(result_df['registered'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('registered Users by weekday')
        plt.axis('equal')  

        plt.subplot(1, 3, 3)
        plt.pie(result_df['cnt'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('total Users by weekday')
        plt.axis('equal')                       

        st.pyplot(fig)


        workingday_mapping = {0: 'no', 1: 'yes'}

        bike_day_df_copy = bike_day_df.copy()
        bike_day_df_copy['workingday'] = bike_day_df_copy['workingday'].map(workingday_mapping)


        result_df = bike_day_df_copy.groupby(by="workingday").agg({
            "casual":  lambda x: (x.sum() / bike_day_df_copy['casual'].sum()) * 100, 
            "registered": lambda x: (x.sum() / bike_day_df_copy['registered'].sum()) * 100, 
            "cnt": lambda x: (x.sum() / bike_day_df_copy['cnt'].sum()) * 100
            })

        labels = result_df.index.astype(str)

        fig = plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.pie(result_df['casual'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Casual Users by workingday')
        plt.axis('equal')  

        plt.subplot(1, 3, 2)
        plt.pie(result_df['registered'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('registered Users by workingday')
        plt.axis('equal')  

        plt.subplot(1, 3, 3)
        plt.pie(result_df['cnt'], labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('total Users by workingday')
        plt.axis('equal')  

        st.pyplot(fig)

        


 

if __name__ == "__main__":
    main()