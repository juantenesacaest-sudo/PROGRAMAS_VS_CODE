from estudiante import Estudiante
from docente import Docente

estudiante=Estudiante("Alex", "Minchala", "0150572600", "0967845202", "alexalva200821@gmail.com", 18, "Cdla.Casa para todos", "TDSU", [8, 9, 7,8,8])
estudiante2=Estudiante("David", "Tenesaca", "0150572601", "0967845203", "david@example.com", 18,"Av. Libertador", "TDSU", [7, 8, 9, 8, 7])
estudiante3=Estudiante("Alexander", "Juela", "0150572602", "0967845204", "Alexander@example.com", 18, "Calle 789", "TDSU", [9, 8, 7, 8, 9])
estudiante4=Estudiante("Andersson", "Bermejo", "0150572603", "0967845205", "Andersson@example.com", 21, "Calle 101", "TDSU", [8, 7, 9, 8, 7])
estudiante5=Estudiante("Alex", "Lumbi", "0150572604", "0967845206", "alexL@example.com", 21, "Calle 102", "TDSU", [7, 9, 8, 8, 9])
print(estudiante,estudiante2,estudiante3,estudiante4,estudiante5,sep="\n",)
print(estudiante.validar_edad(), "promedio:", estudiante.promedio())
print(estudiante2.validar_edad(), "promedio:", estudiante2.promedio())
print(estudiante3.validar_edad(), "promedio:", estudiante3.promedio())
print(estudiante4.validar_edad(), "promedio:", estudiante4.promedio())
print(estudiante5.validar_edad(), "promedio:", estudiante5.promedio())
docente=Docente("Veronica", "Segarra", "0150572605", "0967845207", "veronica@example.com", 30, "Calle 103", "TDSU", 40)
docente2=Docente("Veronica", "Chimbo", "0150572606", "0967845208", "veronica@example.com", 28, "Calle 104", "TDSU", 35)
docente3=Docente("Carmen", "Tacuri", "0150572607", "0967845209", "carmen@example.com", 32, "Calle 105", "TDSU", 45)
docente4=Docente("Diana", "Romero", "0150572608", "0967845210", "diana@example.com", 26, "Calle 106", "TDSU", 30)
docente5=Docente("Iliana", "Tilco", "0150572609", "0967845211", "iliana@example.com", 29, "Calle 107", "TDSU", 38)
docente.calcular_salario()
docente2.calcular_salario()
docente3.calcular_salario()
docente4.calcular_salario()
docente5.calcular_salario()
print(docente,docente2,docente3,docente4,docente5,sep="\n",)

estudiantes = [estudiante, estudiante2, estudiante3, estudiante4, estudiante5]
docentes = [docente, docente2, docente3, docente4, docente5]

for estudiante in estudiantes:
    print(estudiante)

for docente in docentes:
    print(docente)
