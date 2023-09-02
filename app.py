import streamlit as st
import pandas as pd
import time
timestr = time.strftime("%d%m%Y-%H%M%S")

# Load Data Function
def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit Data Editor App")
    
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        data_file = st.file_uploader("Upload CSV",type=["csv"])
        if data_file is not None:
            df = load_data(data_file)
            # Saving Form
            with st.form("editor_form"):
                edited_df = st.data_editor(df)
                save_button = st.form_submit_button("Save Data")
                st.write(dir(data_file))
            if save_button:
                pass
                new_filename = f"{data_file.name} {timestr}.csv"
                final_df = edited_df.to_csv()
                
                st.download_button(label='Download data as CSV',data=final_df,file_name=new_filename,
                                   mime='text/csv')
                
                if save_button:
                    pass
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()