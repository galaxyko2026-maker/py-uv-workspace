

import streamlit as st
import pandas as pd
import os

st.title("학생 정보 입력 및 저장")

CSV_FILE = "students.csv"

# 기존 저장된 데이터 불러오기 (없으면 새로 생성)
if os.path.exists(CSV_FILE):
    df_saved = pd.read_csv(CSV_FILE)
else:
    df_saved = pd.DataFrame(columns=["학번", "이름", "전공"])

st.write("학번, 이름, 전공을 입력하고 저장 버튼을 누르면 한 명씩 추가됩니다.")

col1, col2, col3 = st.columns(3)
with col1:
    student_id = st.text_input("학번")
with col2:
    name = st.text_input("이름")
with col3:
    major = st.text_input("전공")

if st.button("저장하기"):
    student_id = student_id.strip()
    name = name.strip()
    major = major.strip()

    if not (student_id and name and major):
        st.warning("학번, 이름, 전공을 모두 입력해주세요.")
    elif not df_saved.empty and (df_saved["학번"].astype(str) == student_id).any():
        st.error("이미 입력 완료하였습니다.")
    else:
        new_data = [{"학번": student_id, "이름": name, "전공": major}]
        df_new = pd.DataFrame(new_data)
        df_saved = pd.concat([df_saved, df_new], ignore_index=True)
        df_saved.to_csv(CSV_FILE, index=False)
        st.success(f"학생 '{name}'의 정보가 저장되었습니다.")

st.write("### 저장된 전체 학생 정보")
if os.path.exists(CSV_FILE):
    df_saved = pd.read_csv(CSV_FILE)
    st.table(df_saved)
else:
    st.info("아직 저장된 데이터가 없습니다.")
