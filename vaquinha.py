import streamlit as st

# Dados principais
OBJETIVO = 45000.00
CHAVE_PIX = "adao.neto2021@gmail.com"
BANCO_PIX = "Banco Itaú"
DATA_ATUALIZACAO = "16/08/2025"
EMAIL_CONTATO = "adao.neto2021@gmail.com"
TELEFONE_CONTATO = "+55 12 98849-0678"
INSTAGRAM_LINK = "https://www.instagram.com/adao.alvescostaneto"

# Título
st.title("💚 Vaquinha Solidária - Adão Alves da Costa Neto")

# Mensagem principal
st.markdown("""
Estou em estágio 5 de insuficiência renal, com apenas 10% da função dos meus rins.  
Preciso com urgência de um transplante.  
Qualquer ajuda é muito importante neste momento – seja como ajudador ou divulgador.  
Desde já, agradeço de coração pela solidariedade.
""")

# Objetivo
st.subheader(f"🎯 Objetivo: R$ {OBJETIVO:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Chave PIX com campo de cópia
st.markdown("💸 **Chave PIX:**")
st.code(CHAVE_PIX, language="")

st.markdown("🏦 **Banco:** " + BANCO_PIX)

# Instrução para copiar
st.info("📋 Para copiar a chave Pix, clique no campo acima e pressione Ctrl+C (ou toque e segure no celular).")

# Instagram
st.markdown(f"[📲 Instagram: @adaoalvescostaneto]({INSTAGRAM_LINK})")

# Contato
st.markdown(f"📧 {EMAIL_CONTATO}  \n📱 {TELEFONE_CONTATO}")

# Atualização
st.caption(f"📅 Atualizado em: {DATA_ATUALIZACAO}")

# Rodapé
st.markdown("---")
st.markdown("🔁 Compartilhe esta vaquinha e ajude a salvar uma vida!")



