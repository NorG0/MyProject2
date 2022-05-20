
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


from PIL import Image


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

# def runmodel():
# 	cmd = 'python Final_Model.py'
# 	p = subprocess.Popen(cmd, shell=True)


def main():
	"""Simple Login App"""

	st.title("HOẠT ĐỘNG LÀM VIỆC")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		image = Image.open('crashier.jpg')
		st.image(image)
		

	elif choice == "Login":
		st.subheader("Chào Mừng Trở Lại Ca Làm Việc")
		st.markdown("Vui Lòng Đăng Nhập")
		image = Image.open('signin.jpg')
		st.image(image)


		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				file = open ('user.txt','w')
				file.write(username)
				task = st.selectbox("Task",["Dashboard","Profiles","Manage"])
				if username == "norg":
					st.subheader("Thông tin nhân viên")
					st.markdown("Tên: Hoàng Nam Hội")
					st.markdown("Giới Tính: Nam")
					st.markdown("Tuổi: 18")
					st.markdown("Ca làm việc: Sáng ")
					image = Image.open('male.jpg')
					st.image(image,width=300)

				if username == "admin":	
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
# 							cmd = 'python Final_Model.py'
# 							subprocess.Popen(cmd, shell=True)
							
					elif task == "Profiles":
						st.subheader("User Profiles")
						user_result = view_all_users()
						clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
						st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

	elif choice == "Manange":
		st.title("Report Dashboard")


if __name__ == '__main__':
	main()
