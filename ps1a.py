def part_a():
    annual_salary = float(input("Entrez votre salaire annuel: "))
    portion_saved = float(input("Entrez le pourcentage de votre salaire à économiser, sous forme décimale: "))
    total_cost = float(input("Entrez le coût de la maison de vos rêves: "))

    # initialisation
    current_savings = 0
    portion_down_payment = 0.25 * total_cost
    monthly_salary = annual_salary / 12
    current_savings = current_savings + (portion_saved * monthly_salary) + (current_savings * 0.04) / 12
    number_of_months = 1
    while current_savings < portion_down_payment:
        current_savings = current_savings + (portion_saved * monthly_salary) + (current_savings * 0.04) / 12
        number_of_months += 1

    print("Nombre de mois: ", number_of_months)