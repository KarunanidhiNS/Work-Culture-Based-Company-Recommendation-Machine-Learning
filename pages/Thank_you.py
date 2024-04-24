import streamlit as st
import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Culture Based Company Recommendation",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(4vw, 15px);
            font-weight: 500;
            top: 0px;
            right: 15%;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 0.5rem;
        }
    </style>
    <p id="effect">Work Culture Based Company Recommendation</p>
    """,
    height=100,
)


def page_layout():

    st.write("In the modern business landscape, fostering a vibrant work culture is vital for organizational success. This guide offers key recommendations for companies aiming to cultivate an environment that fosters productivity, innovation, and employee well-being. Strong leadership is fundamental, emphasizing clear communication, empathy, and leading by example. Employee engagement is crucial, supported by collaboration, recognition, and professional growth opportunities. Prioritizing work-life balance and well-being through flexible arrangements and support initiatives is essential to prevent burnout. Embracing diversity and inclusion enriches perspectives and drives innovation. Regular feedback mechanisms ensure continuous improvement, fostering a culture of adaptation and success. Overall, by implementing these strategies, companies can create a dynamic work culture where employees are empowered to excel, contributing to sustained organizational growth and success.")
    

    st.write("1. **TCS**")

    st.write("- - - Emphasis on creativity, innovation, and employee well-being.")

    st.write("- - - Encourages employees to pursue passions and explore new ideas through initiatives like 20% time.")
    
    st.write("- - - Fosters a culture of innovation and continuous learning.")

    st.write("2. **Infosys**")

    st.write("- - - Strong emphasis on equality, diversity, and inclusion.")

    st.write("- - - Committed to philanthropy and social responsibility, with initiatives like the 1-1-1 model.")

    st.write("- - - Creates a workplace where every employee feels valued and respected.")

    st.write("2. **Accenture**")

    st.write("- - - Unique approach to work culture emphasizing freedom and responsibility.")

    st.write("- - - Prioritizes hiring highly talented individuals and granting them significant autonomy.")

    st.write("- - - Fosters a culture of accountability, ownership, and transparency.")

# Render page layout
page_layout()


