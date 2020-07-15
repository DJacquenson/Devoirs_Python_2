def part_b():
    annual_salary = float(input("Entrez votre salaire annuel: "))
    portion_saved = float(input("Entrez le pourcentage de votre salaire à économiser, sous forme décimale: "))
    total_cost = float(input("Entrez le coût de la maison de vos rêves: "))
    semi_annual_raise = float(input("Saisissez l'augmentation semi-annuelle, sous forme décimale: "))

    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    down_payment = total_cost * portion_down_payment

    months = 0

    while current_savings < down_payment:
        current_savings *= (1 + (r / 12))
        current_savings += ((annual_salary / 12) * portion_saved)
        months += 1
        if (months % 6) == 0:
            annual_salary *= (1 + semi_annual_raise)

    print("Le nombre de mois est: ", months)