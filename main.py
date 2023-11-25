import streamlit as st
from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2
st.set_page_config(page_title="Gokulan Nithianadam", page_icon="👨‍💻", layout="wide", initial_sidebar_state="auto", menu_items=None)
with open("Gokulan Nithianandam CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
def streamlit_menu():
    selected = option_menu(
            menu_title=None,  # required
            options=["Home","Work", "Portfolio"],  # required
            #icons=["house", "book", "envelope"],  # optional
            #menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "white"},
                "icon": {"color": "orange", "font-size": "1px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#CDF5FD",
                    "font-color": "white",
                },
                "nav-link-selected": {"background-color": "#146C94"},
            }
        )
    return selected


    



selected = streamlit_menu()

if selected == "Home":
    
    
    st.markdown("<h1 style='color: #146C94;'>Hi, I'm Gokulan Nithianandam</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #146C94;'>A creative force dedicated to streamlining workflows through innovative automation solutions. As a specialist in computer vision and control systems, I currently thrive as a software and controls engineer at P2i LTD.</h2>", unsafe_allow_html=True)
    intro = "My journey includes postgraduate studies in Robotics and Autonomous Systems, where I delved deep into the intricate world of cutting-edge technology. My foundation lies in Electrical and Electronics Engineering from my undergraduate studies, providing a solid base for my current endeavors.Beyond the world of technology, I find joy in the simplicity of life. Whether diving into the refreshing waters of a pool, hitting the pavement for a run, or immersing myself in the worlds created by captivating books—I embrace the balance of both the digital and analog aspects of life."
    
    # Use f-string correctly to substitute the variable value
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{intro}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    st.title("")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("github_logo.png")#https://iconmonstr.com/github-1-png/
        hyperlink_text = "GitHub"
        hyperlink_url = "https://github.com/GNithianandam"
        # Create a hyperlink on text using st.markdown
        st.markdown(f"[{hyperlink_text}]({hyperlink_url})", unsafe_allow_html=True)
        
    with col2:
        st.image("linkedin_logo.png")#https://iconmonstr.com/linkedin-3-png/
        # Hyperlink text and URL
        hyperlink_text = "LinkedIn"
        hyperlink_url = "https:www.linkedin.com/in/gokulan-nithianandam"
        # Create a hyperlink on text using st.markdown
        st.markdown(f"[{hyperlink_text}]({hyperlink_url})", unsafe_allow_html=True)
       

    with col3:
        st.image("email_logo.png")#https://iconmonstr.com/email-10-png/
        st.write("g.nithianandam@gmail.com")
    with col4:
        st.image("CV_logo.png")
        st.download_button(label="Download",
                        data=PDFbyte,
                        file_name="Gokulan Nithianandam.pdf",
                        mime='application/octet-stream')    
if selected == "Work":
    st.header("P2i Limited – Oxford, UK.")
    skills = "Siemen's TIA Portal | Profibus | Profinet | .NET | MariaDB | Beijer's IX Developer"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Software and Controls Engineer | June 2023 – Present"):
        st.write("Engineered a robust Electrical Resistivity test software leveraging the .NET framework. The software seamlessly communicates with the Power Supply and Multimeter through SCPI commands, ensuring efficient and precise data acquisition. The acquired results are meticulously computed and stored in a CSV file for convenient analysis and reporting.")            
        st.write("Developed a user-centric Human-Machine Interface (HMI) using Beijer IX Developer for an innovative development machine, placing a strong emphasis on seamless narration. Engineered a sophisticated script facilitating communication with an external database, enabling comprehensive functionality for logging, user management, and recipe management. The HMI adheres meticulously to IEC standards, ensuring a reliable and standardized interface for optimal performance.")
        st.write("Engineered a Time-Based One-Time Password (TOTP) authenticator application utilizing the .NET framework. Seamlessly integrated this app with the existing Human-Machine Interface (HMI) software to enhance authentication processes. The result is a robust and secure solution that ensures improved access control and heightened security measures.")
    st.header("Brillopak Limited – East Peckham, UK.")
    skills = "Omron's Sysmac Studio | Ethercat | Ethernet/IP | Adept Robotics | C# | .NET"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Control Engineer | September 2020 – June 2023"):
        st.write("Demonstrated expertise in developing high-speed pick and place robotic systems from concept to completion using EV+ and C# programming languages.")            
        st.write("Designed and executed control systems for multiple industries, including manufacturing, agriculture, and food production.")
        st.write("Developed and implemented functional designs for safety PLC, control system, and interface to ensure the highest level of safety and efficiency of the robotic systems.")
        st.write("Involved in customer P&ID and FAT phases of the project.")
        st.write("Successfully managed commissioning and installation phases of multiple projects worth over ¬£2 million and completed them before the proposed deadline.")
    with st.expander("Graduate controls engineer September 2018 – September 2020"):
        st.write("Conducted simulations and tests to validate system design and performance prior to sales, ensuring product functionality and quality.")
        st.write("Tested sensors and actuators from various manufacturers to identify the most effective components for improving system performance and accuracy.")
    st.header("Webster Griffin Limited – Crowborough, UK.")
    skills = "Solidworks Electrical | AutoCAD | Python | Microsoft NAV"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Trainee electrical design engineer July 2016 – July 2017"):
        st.write("Designed single-phase and three-phase control systems using Solidworks Electrical and AutoCAD software packages, and created bills of materials using Microsoft Dynamics NAV.")
        st.write("Streamlined the design process and reduced design timescale by developing macros for standard systems and implementing electrical schematic design and panel layout design in one software package.")
        st.write("mproved system design by introducing line drawing and terminal configuration drawing, enhancing understanding of system wiring and sensor position")
        st.write("Developed a simulation software using Python language to demonstrate the system's working concept to clients, enabling the company to showcase the system's functionality and effectiveness.")
if selected == "Portfolio":
    st.header("Sofware development for bolt making machine")
    skills = "Omron sysmac studio | Ethercat | Serial Communication | Servo drives"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Description"):
        st.write("Conducted remote programming and testing of bolt-making machines for an Australian client. Configured Programmable Logic Controllers (PLC) and Human Machine Interfaces (HMI) based on Omron technology. Established serial communication protocols with both facing and drilling machines. Additionally, integrated Omron servo drives for other critical processes.")
    st.header("Barcode detection")
    skills = "Pytorch | Python | Streamlit | Computer Vision"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Description"):
        st.write("Employed an object detection algorithm to train a model specifically designed for detecting barcodes within given objects. Following the training process, successfully deployed the trained model using the Streamlit library for a streamlined and interactive user interface")
    st.header("Simulation of Spent Nuclear Fuel storage")
    skills = "Coppeliasim | Lua"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Description"):
        st.write("Four Niryo robots navigates the rod across three walls and places the rod in a receptacle.")
        hyperlink_text = "Read More"
        hyperlink_url = "https://github.com/GNithianandam/Simulation-of-Spent-Nuclear-Fuel-storage"
        # Create a hyperlink on text using st.markdown
        st.markdown(f"[{hyperlink_text}]({hyperlink_url})", unsafe_allow_html=True)
    st.header("EEG Motor Imagery Classification")
    skills = "Tensorflow | Python | Deep Learning |     Neuroscience"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Description"):
        st.write("A comprehensive study compares four deep learning models and two data augmentation methods for the classification of Motor Imagery tasks")
        hyperlink_text = "Read More"
        hyperlink_url = "https://github.com/GNithianandam/EEG-Motor-Imagery-classification"
        # Create a hyperlink on text using st.markdown
        st.markdown(f"[{hyperlink_text}]({hyperlink_url})", unsafe_allow_html=True)
    st.header("Lunar Lander")
    skills = "Tensorflow | Python | Deep Learning | Reinforcement Learning"
    styled_text = f"<h2 style='color: #146C94; font-size: 20px;'>{skills.replace('|', '&nbsp;&nbsp;&nbsp;')}</h2>"
    st.markdown(styled_text, unsafe_allow_html=True)
    with st.expander("Description"):
        st.write("Using Reinforcement Learning algorithm to solve the lunar lander problem")
        hyperlink_text = "Read More"
        hyperlink_url = "https://github.com/GNithianandam/ReinforcementLearning_Lunar-Landing"
        # Create a hyperlink on text using st.markdown
        st.markdown(f"[{hyperlink_text}]({hyperlink_url})", unsafe_allow_html=True)
    