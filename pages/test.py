import streamlit as st



new_ingredient_1 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient')
if new_ingredient_1:
    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_1])}")
    
    new_ingredient_2 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient2')
    if new_ingredient_2:
        st.write(f"You have selected {new_ingredient_2}")
        
        new_ingredient_3 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient3')
        if new_ingredient_3:
            st.write(f"You have selected {new_ingredient_3}")
            
            new_ingredient_4 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient4')
            if new_ingredient_4:
                st.write(f"You have selected {new_ingredient_4}")
                
                new_ingredient_5 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient5')
                if new_ingredient_5:
                    st.write(f"You have selected {new_ingredient_5}")
                    
                    new_ingredient_6 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient6')
                    if new_ingredient_6:
                        st.write(f"You have selected {new_ingredient_6}")
                        
                        new_ingredient_7 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient7')
                        if new_ingredient_7:
                            st.write(f"You have selected {new_ingredient_7}")
                            
                            new_ingredient_8 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient8')
                            if new_ingredient_8:
                                st.write(f"You have selected {new_ingredient_8}")
                                
                                new_ingredient_9 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient9')
                                if new_ingredient_9:
                                    st.write(f"You have selected {new_ingredient_9}")
                                    
                                    new_ingredient_10 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient10')
                                    if new_ingredient_10:
                                        st.write(f"You have selected {new_ingredient_10}")
                                        
                                        new_ingredient_11 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient11')
                                        if new_ingredient_11:
                                            st.write(f"You have selected {new_ingredient_11}")
                                            
                                            new_ingredient_12 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient12')
                                            if new_ingredient_12:
                                                st.write(f"You have selected {new_ingredient_12}")
