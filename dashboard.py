import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Title of the dashboard
st.set_page_config(page_title="Beginner Store Sales Dashboard", layout="wide")
st.title("Beginner Store Sales Dashboard")

# 2. Data (A simple table created right inside Python)
data = {
    "city": ["Kigali", "Gisenyi", "Huye", "Musanze", "Ngororero", "Karongi", "Muhanga", "Rwamagana"],
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse", "Keyboard", "Monitor"],
    "sales": [10000, 20000, 15000, 25000, 12000, 22000, 17000, 27000],
    "unity_price": [1000, 20, 50, 200, 1200, 25, 55, 210],
    "Clients": [1000, 2000, 3000, 4000, 1500, 2500, 3500, 4500]
}
df = pd.DataFrame(data)

# 3. Side-by-Side Filters
filter_col1, filter_col2 = st.columns(2)

with filter_col1:
    city_options = ["All"] + list(df["city"].unique())
    selected_city = st.selectbox("Choose a city:", options=city_options)

with filter_col2:
    product_options = ["All"] + list(df["product"].unique())
    selected_product = st.selectbox("Choose a product:", options=product_options)

if selected_city != "All":
    df = df[df["city"] == selected_city]

if selected_product != "All":
    df = df[df["product"] == selected_product]

# 4. KPI Summary Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${df['sales'].sum():,}")
col2.metric("Total Products Sold", f"{df['product'].nunique()}")
col3.metric("Average Unity Price", f"${df['unity_price'].mean():.2f}" if not df.empty else "$0.00")
col4.metric("Total Clients", f"{df['Clients'].sum():,}")

# 5. Row 1: Chart 1 (Left) & Chart 2 (Right)
chart1, chart2 = st.columns(2)

with chart1:
    fig1 = px.bar(
        df,
        x="city",
        y="Clients",
        color="product",
        title="Clients by City and Product"
    )
    st.plotly_chart(fig1, use_container_width=True)

with chart2:
    fig2 = px.pie(
        df,
        names="product",
        values="sales",
        title="Sales Distribution by Product"
    )
    st.plotly_chart(fig2, use_container_width=True)

# 6. Row 2: Chart 3 (Left) & Chart 4 (Right)
chart3, chart4 = st.columns(2)

with chart3:
    fig3 = px.bar(
        df,
        x="sales",
        y="city",
        color="city",
        orientation="h",
        text_auto=True,
        title="Total Sales Ranking by City"
    )
    st.plotly_chart(fig3, use_container_width=True)

with chart4:
    fig4 = px.scatter(
        df,
        x="unity_price",
        y="sales",
        size="Clients",
        color="product",
        hover_name="city",
        title="Sales vs. Unit Price (Bubble Size = Clients)"
    )
    st.plotly_chart(fig4, use_container_width=True)

st.dataframe(df, use_container_width=True)
