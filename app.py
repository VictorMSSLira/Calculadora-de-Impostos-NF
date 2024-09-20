import customtkinter as ctk
import locale

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# FUNÇÕES ================================================================
def Operacao():
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    valor_desconto = radio_var.get()
    if valor_desconto == "outros":
        valor_desconto = outros_desconto.get()
    try:
        valor_desconto = float(valor_desconto) / 100  # Convertendo para porcentagem
        total = valor_coletado.get()
        # TRATAR VALOR
        try:
            total = total.replace(".", "")
            total = total.replace(",", ".")
            total = float(total)

            v1 = total * valor_desconto
            v1_formatado = locale.currency(v1, grouping=True)
            v2 = total - v1
            v2_formatado = locale.currency(v2, grouping=True)

            resultado_liquido.configure(state="normal")
            resultado_liquido.delete("0.0", "end")
            resultado_liquido.insert("0.0", f"Líquido: {v2_formatado}")
            resultado_liquido.configure(state="disabled", fg_color="#C9DAF8")
            resultado_desconto.configure(state="normal")
            resultado_desconto.delete("0.0", "end")
            resultado_desconto.insert("0.0", f"Desconto: {v1_formatado}")
            resultado_desconto.configure(state="disabled", fg_color="#FFDDC1")
        except:
            resultado_desconto.configure(
                text="Valor inválido.\nDigite novamente!")
    except:
        resultado_desconto.configure(text="Selecione um valor\nde desconto!")

# INÍCIO ==================================================================
app = ctk.CTk()
app.title("Calculadora de Impostos")
app.geometry("380x550")

# TEXTO TOPO ==============================================================
texto = ctk.CTkLabel(app, text="Digite o Valor e Selecione o Desconto", font=(
    "Helvetica", 18), text_color="#02b848")
texto.pack(padx=10, pady=10)

# INPUT DO VALOR ==========================================================
valor_coletado = ctk.CTkEntry(
    app, placeholder_text="Digite o valor em reais", width=300, justify="center", font=("Consolas", 22))
valor_coletado.pack(padx=10, pady=10)

# BOTÕES DE RADIO =========================================================
radio_var = ctk.StringVar()
radio_var.set("0.012")
radio_024 = ctk.CTkRadioButton(
    app, text="0,24%", value="0.0024", variable=radio_var)
radio_024.pack(pady=10)
radio_12 = ctk.CTkRadioButton(
    app, text="1,2%", value="0.012", variable=radio_var)
radio_12.pack(pady=10)
radio_48 = ctk.CTkRadioButton(
    app, text="4,8%", value="0.048", variable=radio_var)
radio_48.pack(pady=10)
radio_outros = ctk.CTkRadioButton(
    app, text="Outros (%)", value="outros", variable=radio_var)
radio_outros.pack(pady=10)

# INPUT PARA OUTROS DESCONTOS =============================================
outros_desconto = ctk.CTkEntry(
    app, placeholder_text="Digite o desconto em %", width=300, justify="center", font=("Consolas", 22))
outros_desconto.pack(padx=10, pady=10)

# BOTÃO CALCULAR ==========================================================
bt_calcular = ctk.CTkButton(app, text="Calcular", command=Operacao)
bt_calcular.pack(padx=10, pady=10)

# APRESENTAR RESULTADO ====================================================
resultado_liquido = ctk.CTkTextbox(
    app, width=330, height=45, font=("Consolas", 22, "bold"), text_color="#0015ff")
resultado_liquido.pack(padx=10, pady=10)

resultado_desconto = ctk.CTkTextbox(
    app, width=330, height=45, font=("Consolas", 22, "bold"), text_color="#e63e00")
resultado_desconto.pack(padx=10, pady=10)

# FAZER APARECER A JANELA (ULTIMA COISA)===================================
app.mainloop()
