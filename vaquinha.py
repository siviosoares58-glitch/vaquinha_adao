import streamlit as st
import datetime

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

# Mensagem
st.markdown("""
Estou em estágio 5 de insuficiência renal, com apenas 10% da função dos meus rins.  
Preciso com urgência de um transplante.  
Qualquer ajuda é muito importante neste momento – seja como ajudador ou divulgador.  
Desde já, agradeço de coração pela solidariedade.
""")

# Objetivo
st.subheader(f"🎯 Objetivo: R$ {OBJETIVO:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Chave PIX com botão de cópia automática
st.markdown(f"""
    <div style="margin-top: 10px;">
        <label style="font-weight: bold;">💸 Chave PIX:</label><br>
        <input type="text" value="{CHAVE_PIX}" id="pixInput" readonly style="width: 300px; padding: 8px; font-size: 16px; margin-top: 5px;">
        <button onclick="copyPix()" style="margin-left: 10px; padding: 8px; font-size: 16px;">📋 Copiar</button>
    </div>
    <div style="margin-top: 10px;">
        <strong>🏦 Banco:</strong> {BANCO_PIX}
    </div>

    <script>
    function copyPix() {{
        var copyText = document.getElementById("pixInput");
        copyText.select();
        copyText.setSelectionRange(0, 99999); // Para dispositivos móveis
        document.execCommand("copy");
        alert("✅ Chave PIX copiada: " + copyText.value);
    }}
    </script>
""", unsafe_allow_html=True)

# Instagram
st.markdown(f"[📲 Instagram: @adaoalvescostaneto]({INSTAGRAM_LINK})")

# Contato
st.markdown(f"📧 {EMAIL_CONTATO}  \n📱 {TELEFONE_CONTATO}")

# Atualização
st.caption(f"📅 Atualizado em: {DATA_ATUALIZACAO}")

# Rodapé
st.markdown("---")
st.markdown("🔁 Compartilhe esta vaquinha e ajude a salvar uma vida!")

