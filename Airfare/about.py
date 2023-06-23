import streamlit as st

def main():
    
    st.set_page_config(page_title="SkySpy")
    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.postimg.cc/3N1V8nYd/airplane.jpg");
             background-attachment: fixed;
             background-size: 100% 100%;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    st.markdown("<h2 style='text-align: center; font-style: italic;'>Welcome to SkySpy!</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<span style='font-size: 24px;'>Experience a <span style='color: blue; font-style: italic;'>stress-free</span> journey with our app - <span style='color: blue; font-style: italic;'>no hidden costs!</span></span>", unsafe_allow_html=True)
    st.write("")
    
    st.markdown("<span style='font-size: 24px;'>Simply fill in a few details to easily compare airfares from different airlines and <span style='color: blue; font-style: italic;'>find yourself the best deal.</span>", unsafe_allow_html=True)
    st.write("")
    
    st.markdown("---")
    
if __name__ == '__main__':
    main()