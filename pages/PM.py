# 以下を「app.py」に書き込み
import streamlit as st
import numpy as np
import pandas as pd

# ---------- 変数の記述による表示（magic command） ----------
st.title("LancersAgent PM")
"""
 登録案件 528 件（5月21日現在）
"""

df = pd.read_csv('LancersAgent_df_pm.csv')

df
# ---------- サイドバー ----------
st.title("サイドバーの選択結果")

# ---------- 職種サイドバー ----------
pd.set_option('display.max_rows', 900)
value_counts = df["職種"].value_counts()
df1 = pd.DataFrame({'職種':value_counts.index, '数':value_counts.values})
selected_side = st.sidebar.selectbox(
    "どの職種を選びますか？",
    df1
    )
# st.write("あなたは" + str(selected_side) + "を選びました！")
df1_sel = df1[df1["職種"] == selected_side]
st.write(df1_sel)
# count = df1_sel["数"].astype(int)
# st.write(count)

df[df['職種'] == selected_side]

# ---------- スキルサイドバー ----------
pd.set_option('display.max_rows', 900)
value_counts = df["スキル"].value_counts()
df2 = pd.DataFrame({'スキル':value_counts.index, '数':value_counts.values})
selected_side = st.sidebar.selectbox(
    "どのスキルを選びますか？",
    df2
    )
# st.write("あなたは" + str(selected_side) + "を選びました！")
df2_sel = df2[df2["スキル"] == selected_side]
st.write(df2_sel)
# count2 = df2_sel["数"].astype(int)
# st.write(count2)

df[df['スキル'] == selected_side]

# ---------- 職場サイドバー ----------
pd.set_option('display.max_rows', 900)
value_counts = df["職場"].value_counts()
df3 = pd.DataFrame({'職場':value_counts.index, '数':value_counts.values})
selected_side = st.sidebar.selectbox(
    "どの職場を選びますか？",
    df3
    )
# st.write("あなたは" + str(selected_side) + "を選びました！")
df3_sel = df3[df3["職場"] == selected_side]
st.write(df3_sel)
# count3 = df3_sel["数"].astype(int)
# st.write(count3)

df[df['職場'] == selected_side]

# ---------- 月額報酬サイドバー ----------
pd.set_option('display.max_rows', 900)
value_counts = df["月額報酬"].value_counts()
df4 = pd.DataFrame({'月額報酬':value_counts.index, '数':value_counts.values})
selected_side = st.sidebar.selectbox(
    "どの月額報酬を選びますか？",
    df4
    )
# st.write("あなたは" + str(selected_side) + "を選びました！")
df4_sel = df4[df4["月額報酬"] == selected_side]
st.write(df4_sel)
# count4 = df4_sel["数"].astype(int)
# st.write(count4)

df[df['月額報酬'] == selected_side]

# ---------- スキル・言語・FWサイドバー ----------
pd.set_option('display.max_rows', 900)
value_counts = df["スキル・言語・FW"].value_counts()
df5 = pd.DataFrame({'スキル・言語・FW':value_counts.index, '数':value_counts.values})
selected_side = st.sidebar.selectbox(
    "どのスキル・言語・FWを選びますか？",
    df5
    )
# st.write("あなたは" + str(selected_side) + "を選びました！")
df5_sel = df5[df5["スキル・言語・FW"] == selected_side]
st.write(df5_sel)
# count5 = df5_sel["数"].astype(int)
# st.write(count5)

df[df['スキル・言語・FW'] == selected_side]

# ---------- 勤務日数詳細サイドバー ----------
pd.set_option('display.max_rows', 900)
value_counts = df["勤務日数詳細"].value_counts()
df6 = pd.DataFrame({'勤務日数詳細':value_counts.index, '数':value_counts.values})
selected_side = st.sidebar.selectbox(
    "どの勤務日数詳細を選びますか？",
    df6
    )
# st.write("あなたは" + str(selected_side) + "を選びました！")
df6_sel = df6[df6["勤務日数詳細"] == selected_side]
st.write(df6_sel)
# count6 = df6_sel["数"].astype(int)
# st.write(count6)

df[df['勤務日数詳細'] == selected_side]