# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
# from st_btn_select import st_btn_select

LOGGER = get_logger(__name__)


def run():

  st.set_page_config(
      page_title="Questões Olimpíadas",
      page_icon=":fire:",
  )

  ### DADOS E DATABASE

  # Lê CSV Teste. Futurely replace with DB Connection
  df = pd.read_csv("questoes_teste.csv", sep=",")

  #
  lista_olimpiadas = list(df["olimpiada"].unique())
  lista_nivel = list(df["nivel"].unique())
  lista_fases = list(df["nivel"].unique())
  lista_assuntos = list(df["assunto"].unique())


  ### FUNÇÕES 

  # Function to display box with question information. (TESTANDO BOTÕES AINDA) 
  def question_box (questao) :

      # Seção Enunciado

      enunciado = questao["enunciado"]
      solucao = questao["solucao"]
      resposta_correta = questao["resposta_correta"]

      item_a=questao["item_a"]
      item_b=questao["item_b"]
      item_c=questao["item_c"]
      item_d=questao["item_d"]
      item_e=questao["item_e"]

      itens = [item_a, item_b, item_c, item_d, item_e]
      itens_com_label = [f"A) {item_a}", f"B) {item_b}", f"C) {item_c}", f"D) {item_d}", f"E) {item_e}"]

      
      c = st.container()
      c.subheader("Enunciado")
      c.write(f"{enunciado}")

      
      alternativa_escolhida = st.radio("Escolha a alternativa correta: ", itens_com_label, index=None, key=f"Alternativas_{questao['id']}")

      submit_ans = st.button("Checar resposta", key=f"BotaoEnvioAlternativas_{questao['id']}a")

      
          
      if submit_ans :
          print(alternativa_escolhida)



      c.write(f"A) {item_a}")
      c.write(f"B) {item_b}")
      c.write(f"C) {item_c}")
      c.write(f"D) {item_d}")
      c.write(f"E) {item_e}")


      # Seção Gabarito

      with st.expander(":eye:   VER SOLUÇÃO"):
          st.subheader("Solução:")
          st.write(f"Resposta: {resposta_correta.upper()}")
          st.write(f"{solucao}")


  ### SIDEBAR

  ### Cria Sidebar com formulário para escolher filtros das questões. Possivelmente causando erro. ###
  with st.sidebar.form(key="filtro"):
      olimpiada = st.selectbox("Olimpíada", lista_olimpiadas)
      nivel = st.selectbox("Nível", lista_nivel)

      fase = st.selectbox("Fase", lista_fases)
      assunto = st.selectbox("Assunto", lista_assuntos)

      submit = st.form_submit_button("Filtrar questões")



  if submit :
      questoes_filtradas = df[
          (df["olimpiada"]==olimpiada)
          & (df["assunto"]==assunto)
          & (df["nivel"]==nivel)
          & (df["fase"]==fase)
      ]

      numero_resultados = len(questoes_filtradas)

      st.header(f"Encontramos {numero_resultados} questões!")

      for index, questao in questoes_filtradas.iterrows() :
          question_box(questao)
          st.divider()



if __name__ == "__main__":
    run()
