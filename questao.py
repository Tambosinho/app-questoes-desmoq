

# Enunciado, alternativas, resposta correta, solução
class Questao ():
    def __init__(self, enunciado, alt_a, alt_b, alt_c, alt_d, alt_e, resposta_correta, solucao):
        self.enunciado = enunciado
        self.alt_a = alt_a
        self.alt_b = alt_b
        self.alt_c = alt_c
        self.alt_d = alt_d
        self.alt_e = alt_e
        self.alternativas = [alt_a, alt_b, alt_c, alt_d, alt_e]
        self.resposta_correta = resposta_correta
        self.solucao = solucao


    def ExibirQuestao(self):
        c = st.container()
        c.subheader("Enunciado")
        c.write(f"{enunciado}")
        resposta_escolhida = st_btn_select((f"A) {item_a}", f"B) {item_b}", f"C) {item_c}", f"D) {item_d}", f"E) {item_e}"))

    def ExibirGabarito(self) :
        st.subheader("Solução:")
        st.write(f"Resposta: {resposta_correta.upper()}")
        st.write(f"{solucao}")


    
    


