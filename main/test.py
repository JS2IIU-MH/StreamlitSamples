''' Streamlit Sample Code
    run
    $ streamlit run {this_file.py}
    then, streamlit UI will be shown on the web browser
'''
# streamlit run sample.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st


def main():
    ''' Streamlit Sample Code '''

    st.title('Hello')
    st.write('print string')

    # DataFrame
    st.write('## DataFrame')
    df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]], columns=['col1', 'col2', 'col3'])
    st.write('### table')
    st.table(df)
    st.write('### dataframe')
    st.dataframe(df)

    # latex
    st.write('## LaTeX')
    my_latex_formula = [
        r'S = \sum^{N}_{i=0}a_{n}',
        r'e^{i\theta} = \cos \theta + i \sin \theta',
        r'i\hbar\frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2}+V(x)\psi'
        ]

    for i in range(3):
        st.latex(my_latex_formula[i])

    # graph
    st.write('## streamlit built-in graph')
    x = np.arange(0, 100)
    y = np.power(x, 2)

    df2 = pd.DataFrame()
    df2['x'] = x
    df2['y'] = y

    st.write('### line_chart')
    st.line_chart(data=df2)
    st.write('### area_chart')
    st.area_chart(data=df2)
    st.write('### bar_chart')
    st.bar_chart(data=df2)

    # matplotlib
    st.write('## matplotlib scatter')
    fig, ax = plt.subplots()
    ax.scatter(x=df2['x'], y=df2['y'], label='scatter sample plot')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.grid()
    ax.legend()

    st.pyplot(fig)

    # checkbox
    st.write('## checkbox')
    if st.checkbox('Coffee'):
        st.write('go to Starbacks')

    # selectbox
    st.write('## selectbox')
    select_items = ['Apple', 'Facebook', 'Google', 'Amazon', 'Tesla']
    ret = st.selectbox('choose one', select_items)
    st.write(ret)

    # dropdownlist
    st.write('## dropdown list')
    ret2 = st.multiselect('choose all you like', select_items)
    st.write(ret2)

    # split multi columns
    st.write('## columns')
    left_column, right_column = st.columns(2)

    if left_column.checkbox('check left column'):
        left_column.write('left column checked')

    if right_column.checkbox('check right column'):
        right_column.write('right column checked')

    # radio button
    st.write('## Radio button')
    ret3 = st.radio('choose one from here', select_items)
    st.write(f'You got {ret3}')

    # Number input
    st.write('## Number input')
    ret4 = st.number_input('put number here:', min_value=0, max_value=10, step=1)
    st.write(f'your number * 2 = {ret4 * 2}')

    # Button element
    st.write('## Button')
    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")


if __name__ == '__main__':
    main()
