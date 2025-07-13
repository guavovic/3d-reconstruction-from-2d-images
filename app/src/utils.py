def log_message(log_label, message):
    """
    Atualiza o log na interface gráfica.
    """
    log_label.config(text=f"{message}")
    log_label.update_idletasks()