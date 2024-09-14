import customtkinter
import locale


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


# FUNÇÕES ================================================================
def Operacao():
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    valor_desconto = radio_var.get()
    try:
        valor_desconto = float(valor_desconto)
        total = valor_coletado.get()
        # TRATAR VALOR
        try:
            total = total.replace(",", ".")
            total = float(total)

            v1 = total*valor_desconto
            v1_formatado = locale.currency(v1, grouping=True)
            v2 = total - v1
            v2_formatado = locale.currency(v2, grouping=True)

            resultado_liquido.delete("0.0", "end")
            resultado_liquido.insert("0.0", f"Líquido: {v2_formatado}")
            resultado_desconto.delete("0.0", "end")
            resultado_desconto.insert("0.0", f"Desconto: {v1_formatado}")
        except:
            resultado_desconto.configure(
                text="Valor inválido.\nDigite novamente!")
    except:
        resultado_desconto.configure(text="Selecione um valor\nde desconto!")


# INÍCIO ==================================================================
app = customtkinter.CTk()
app.title("Calculadora de Impostos")
app.geometry("320x400")


# TEXTO TOPO ==============================================================
texto = customtkinter.CTkLabel(app, text="Digite o Valor e Selecione o Desconto", font=(
    "Helvetica", 16), text_color="#02b848")
texto.pack(padx=10, pady=10)
# 50FA7B
# INPUT DO VALOR ============================================-=============
valor_coletado = customtkinter.CTkEntry(
    app, placeholder_text="Digite o valor em reais", width=250, justify="center", font=("Consolas", 18))
valor_coletado.pack(padx=10, pady=10)

# BOTÕES DE RADIO =========================================================
radio_var = customtkinter.StringVar()
radio_var.set("0.012")
radio_024 = customtkinter.CTkRadioButton(
    app, text="0,24%", value="0.0024", variable=radio_var)
radio_024.pack(pady=10)
radio_12 = customtkinter.CTkRadioButton(
    app, text="1,2%", value="0.012", variable=radio_var)
radio_12.pack(pady=10)
radio_48 = customtkinter.CTkRadioButton(
    app, text="4,8%", value="0.048", variable=radio_var)
radio_48.pack(pady=10)

# BOTÃO CALCULAR ==========================================================
bt_calcular = customtkinter.CTkButton(app, text="Calcular", command=Operacao)
bt_calcular.pack(padx=10, pady=10)

# APRESENTAR RESULTADO ====================================================
resultado_liquido = customtkinter.CTkTextbox(
    app, width=300, height=30, font=("Consolas", 18, "bold"), text_color="#0015ff")
resultado_liquido.pack(pady=10)
#7389ec
resultado_desconto = customtkinter.CTkTextbox(
    app, width=300, height=30, font=("Consolas", 18, "bold"), text_color="#e63e00")
resultado_desconto.pack(pady=10)



# FAZER APARECER A JANELA (ULTIMA COISA)===================================
app.mainloop()
