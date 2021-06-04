# streamlit run main.py をターミナルから実行させ
# streamlitを起動

import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')

'START!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここに右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

option = st.text_input('あなたの趣味は？')
text = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味は', option, 'です。'
'コンディション:', text, 'です'
option = st.selectbox(
    '好きな数字を教えて下さい',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.JPG')
#     st.image(img, caption='うちのネコ', use_column_width=True)
