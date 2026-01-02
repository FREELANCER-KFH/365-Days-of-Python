# Reto: Lógica de selección de mensaje
def get_personal_message(user, hour):
    # Usamos variables para definir el estado
    if hour < 12:
        status = "Buenos días"
    else:
        status = "Buenas tardes/noches"
    
    return f"{status}, {user}."

print(get_personal_message("FREELANCER-KFH", 14))
