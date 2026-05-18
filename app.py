import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Nobel Dashboard")

st.title("🏆 Nobel Laureates Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if "laureate_type" in df.columns:

        type_data = (
            df.groupby("laureate_type")
              .size()
              .reset_index(name="count")
        )

        colors = {
            "Individual": "#3498db",
            "Organization": "#e67e22"
        }

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            type_data["laureate_type"],
            type_data["count"],
            color=[
                colors.get(x, "#95a5a6")
                for x in type_data["laureate_type"]
            ]
        )

        ax.set_title("Nobel Laureates by Type")
        ax.set_xlabel("Laureate Type")
        ax.set_ylabel("Total Count")

        st.pyplot(fig)

    else:
        st.error("Column 'laureate_type' not found")

else:
    st.info("Please upload a CSV file")
