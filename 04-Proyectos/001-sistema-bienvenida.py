# Proyecto: Generador de Perfil de Inicio de Reto
def start_challenge(user, day):
    title = "--- INICIO DE JORNADA ---"
    footer = "-" * len(title)
    
    print(title)
    print(f"Participante: {user}")
    print(f"Progreso Actual: Día {day}")
    print(footer)

current_user = "FREELANCER-KFH"
current_day = 1
start_challenge(current_user, current_day)
