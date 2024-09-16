import streamlit as st
from datetime import datetime
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    st.title("Sistema de CRM e Vendas - Frontend")
    email = st.text_input("E-mail")
    data = st.date_input("Data da venda")
    hora = st.time_input("Hora da venda")
    valor = st.number_input("Valor da venda")
    quantidade = st.number_input("Quantidade")
    produto = st.selectbox("Produto", ["Produto 1", "Produto 2", "Produto 3"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            st.write("***Dados da venda***")
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Erro {e}")


if __name__ == "__main__":
    main()