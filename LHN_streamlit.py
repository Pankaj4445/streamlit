import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import plotly.graph_objects as go

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Dashboard")
#st.markdown("The dashboard will help a researcher to get to know \
#more about the given datasets and it's output")
#st.sidebar.title("Select Visual Charts")
#st.sidebar.markdown("Select the Charts/Plots accordingly:")

# ---- READ EXCEL ----
# @st.cache
# def get_data_from_excel():
#     # df = pd.read_excel(
#     #     io="supermarkt_sales.xlsx",
#     #     engine="openpyxl",
#     #     sheet_name="Sales",
#     #     skiprows=3,
#     #     usecols="B:R",
#     #     nrows=1000,
#     # )
    #df = pd.read_excel(r"C:\Users\User\Downloads\amazon_airConditioner_OP (1).xlsx")
    # # Add 'hour' column to dataframe
    # #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    # return df

#df = get_data_from_excel()
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # raw_dataf = pd.DataFrame(df)
    # recno1 = raw_dataf["Filter_By"].tolist()
    # for i in range(len(recno1)):
    #     recno1[i] = str(recno1[i]) + "'"
#st.dataframe(df)

# ---- SIDEBAR ----
#     chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
#                                         ('Line Chart', 'Bar Chart', 'Pie Chart'))
    #st.sidebar.checkbox("Show Analysis by Smoking Status", True, key=1)

    st.sidebar.header("Please Filter Here:")
    channel = st.sidebar.multiselect(
        "Select the Channel:",
        options=df["Channel"].unique(),
        #options=df["channel "].unique(),
        default=df["Channel"].unique(),
    )

    Category_Name = st.sidebar.multiselect(
        "Select the Category:",
        options=df["Category_Name"].unique(),
        default=df["Category_Name"].unique(),
    )

    # pricetype = st.sidebar.multiselect(
    #     "Select the PriceType:",
    #     options=df["P4_Sale_Price"].unique(),
    #     default=df["P4_Sale_Price"].unique()
    # )

    # filter_by = st.sidebar.multiselect(
    #     "Select Filter: ",
    #     options=df["Filter_By"].unique(),
    #     default=df["Filter_By"].unique()
    #
    # )


    filter_by = st.sidebar.multiselect('Select Filter:',
                                        ('Brands','Discount', 'Discount Range'))
    #filter_by = 'Brands'


    df_selection = df.query("Channel== @channel   & Category_Name == @Category_Name & Filter_By == @filter_by") #P4_Sale_Price == @pricetype
    #st.dataframe(df_selection)
    Filter_Name = st.sidebar.multiselect(
        "Select FilterName: ",
        options=df_selection["Filter_Name"].unique(),

    )

    # if st.checkbox("Select ALL"):
    #     Filter_Name = st.sidebar.multiselect(
    #     "Select FilterName: ",
    #     options=df_selection["Filter_Name"].unique(),
    #     default=df_selection["Filter_Name"].unique(),)
    # else:
    #     Filter_Name = st.sidebar.multiselect(
    #         "Select FilterName: ",
    #         options=df_selection["Filter_Name"].unique(),
    #
    #     )
    #Filter_Name = st.sidebar.multiselect("Select FilterName:", ("LEVI'S", "LEVIS", "Puma", "AND", "AND girl", "NEXT 2 SKIN", "next", "Next One", "Next"))
    df_selection1 = df_selection.query("Filter_Name ==@Filter_Name")
    st.dataframe(df_selection1)
    #
    # # ---- MAINPAGE ----
    # Price = df_selection["P4_Sale_Price"]
    # MRP = df_selection["P4_MRP"]
    filter_count = df_selection1["Filter_Count"]
    filter = df_selection1["Filter_Name"]
    #brands = df_selection["P4_Brand"]
    #count = len(df_selection["P4_Brand"])
    totalfiltercount = sum(df_selection1["Filter_Count"])
    totalcount = sum(df["Filter_Count"])
    percent = (totalfiltercount/totalcount)*100

    # The plot
    fig1 = go.Figure(
        go.Pie(
            labels=filter,
            values=filter_count,
            hoverinfo="label+percent",
            textinfo="value"
        ))




    # fig2 = go.Figure()
    # fig2.add_trace(go.Scatter(x=[i for i in range(count)], y=df["P4_Sale_Price"], name="Sale_Price", mode="lines"))
    # fig2.add_trace(go.Scatter(x=[i for i in range(count)], y=df["P4_MRP"], name="MRP", mode="lines"))
    # fig2.update_layout(
    #     title="Prices", xaxis_title="Record No", yaxis_title="Rs."
    # )
    # st.plotly_chart(fig2)
    #fig2.show()

    # left_column, middle_column = st.columns(2)
    # with left_column:
    #     st.subheader("Total Products Count:")
    #     st.subheader(f" {totalfiltercount:,}")
    # with middle_column:
    #     st.subheader("Data shown :")
    #     st.subheader(f"{percent}", "%")

    st.header("Pie chart")
    st.plotly_chart(fig1)

    #
    # if chart_visual == 'Line Chart':
    #     st.line_chart(Price)
    # elif chart_visual == 'Bar Chart':
    #     st.bar_chart(Price, use_container_width=True)
    # elif chart_visual == 'Pie Chart':
    #     st.header("Pie chart")
    #     st.plotly_chart(fig1)

# TOP KPI's
#     pricebyproductline = (
#     df_selection.groupby(by=["SKU_ID"]).sum()[["P4_Sale_Price"]].sort_values(by="P4_Sale_Price")
#     )


