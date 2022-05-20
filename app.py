import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px




task = st.selectbox("Task",["Dashboard","Profiles","Manage"])
def main():
    st.title("HOẠT ĐỘNG LÀM VIỆC")
    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)
    task = st.selectbox("Task",["Dashboard","Profiles","Manage"])
    if choice == "Home":
        if task == "Dashboard":
            st.subheader("Báo Cáo Hôm Nay")
            st.title("Biểu Đồ Báo Cáo")
            data = pd.read_csv("tt.csv")
            chart_visual = st.sidebar.selectbox('Chọn Loại Biểu Đồ',
                            ('Biểu đồ cột', 'Biểu đồ tròn'))
            
            selected_status = st.sidebar.selectbox('Chọn Trạng thái',
                            options = ['KhongNghiemTuc',
                                        'NghiemTuc', 'VuiVe',
                                        'KhoChiu'])
            fig = go.Figure()
            if chart_visual == 'Biểu đồ cột':
                if selected_status == 'KhongNghiemTuc':
                    fig.add_trace(go.Bar(x = data.name, y = data.KhongNghiemTuc,
                        name = 'KhongNghiemTuc'))
                    st.plotly_chart(fig, use_container_width=True)
                if selected_status == 'NghiemTuc':
                    fig.add_trace(go.Bar(x = data.name, y = data.NghiemTuc,
                            name = 'NghiemTuc'))
                    st.plotly_chart(fig, use_container_width=True)
                if selected_status == 'VuiVe':
                    fig.add_trace(go.Bar(x = data.name, y = data.VuiVe,	
                        name = 'VuiVe'))
                    st.plotly_chart(fig, use_container_width=True)
                if selected_status == 'KhoChiu':
                    fig.add_trace(go.Bar(x=data.name, y=data.KhoChiu,
                        name="KhoChiu"))
                    st.plotly_chart(fig, use_container_width=True)
            if chart_visual =='Biểu đồ tròn':
                if selected_status == 'KhongNghiemTuc':
                    fig = px.pie(data, values='KhongNghiemTuc', names='name')
                    st.plotly_chart(fig, use_container_width=True)
                if selected_status == 'NghiemTuc':
                    fig = px.pie(data, values='NghiemTuc', names='name')
                    st.plotly_chart(fig, use_container_width=True)
                if selected_status == 'VuiVe':
                    fig = px.pie(data, values='VuiVe', names='name')
                    st.plotly_chart(fig, use_container_width=True)
                if selected_status == 'KhoChiu':
                    fig = px.pie(data, values='KhoChiu', names='name')
                    st.plotly_chart(fig, use_container_width=True)
                            
        elif task == "Manage":
            if st.button("Run Model"):
                st.info("Model is running")


        elif choice == "Manange":
            st.title("Report Dashboard")


if __name__ == '__main__':
	main()
