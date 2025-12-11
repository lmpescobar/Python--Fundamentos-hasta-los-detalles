is_student = False

if is_student:
    print("Licencia de estudiante")
else:
    print("Licencia normal")

# Versión en una línea:
get_license = "Licencia de estudiante" if is_student else "Licencia normal"

print("get_license")