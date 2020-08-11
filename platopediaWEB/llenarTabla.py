def llenar():
    from appPlatopedia.models import Group
    from appPlatopedia.models import Food
    from appPlatopedia.models import Vitamins
    from appPlatopedia.models import Value_Vitamins
    from appPlatopedia.models import Minerals
    from appPlatopedia.models import Value_Minerals
    from appPlatopedia.models import PrincipalNutriments
    from appPlatopedia.models import Value_PrincipalNutriments
    import pandas as pd
    import numpy as np
    path = "food.csv"
    df = pd.read_csv(path)
    # Group
    groups = df.FoodGroup.unique()
    list_group = [Group.objects.create(name=group_name) for group_name in groups]
    #"Se crea lista de objetos Group y se almacena
    #Food
    fk_group = []  # Se almacena el indice del grupo
    for item_number in range(df.shape[0]):
        group_item = df.FoodGroup.iloc[item_number]
        fk_group.append(
            np.where(groups == group_item)[0][0]
        )  # identifica el indice del grupo
    df_food = df.iloc[:, 2:6]  # Toma las columnas de Food
    n_rows=df_food.shape[0]
    list_food = []  # Se guardaran los objetos de la tabla food
    for row in range(n_rows):  # Llena la tabla Food
        list_food.append(
            Food.objects.create(
                description=df_food.iloc[row, 0],
                common_name=df_food.iloc[row, 1],
                brand=df_food.iloc[row, 2],
                scientificname=df_food.iloc[row, 3],
                group=list_group[fk_group[row]],
            )
        )
    # Vitamins
    vitamins = df.iloc[:, 12:21]
    list_vitamins = [
        Vitamins.objects.create(name=vitamin_name) for vitamin_name in vitamins
    ]
    # Value_Vitamins
    value_vitamins = vitamins.stack()  # transforma los datos en serie
    value_vitamin = []  # aqui guardaremos los valores de vitaminas del df
    for val in value_vitamins:
        value_vitamin.append(val)
    i = 0
    list_value_vitamins = []  # se guardan objetos
    for row in range(df.shape[0]):
        for col in range(len(list_vitamins)):
            list_value_vitamins.append(
                Value_Vitamins.objects.create(
                    food=list_food[row], vitamins=list_vitamins[col], value=value_vitamin[i]
                )
            )
            i += 1
    # Minerals
    minerals = df.iloc[:, 21:]
    list_minerals = [
        Minerals.objects.create(name=mineral_name) for mineral_name in minerals
    ]

    #"SE CREA LA LISTA DE OBJETOS MINERALS Y SE LLENA LA BD
    # Value_Minerals
    value_minerals = minerals.stack()  # transforma los datos en serie
    value_mineral = []  # aqui guardaremos los valores de vitaminas del df
    for val in value_minerals:
        value_mineral.append(val)
    i = 0
    list_value_minerals = []
    for row in range(df.shape[0]):
        for col in range(len(list_minerals)):
            list_value_minerals.append(
                Value_Minerals.objects.create(
                    food=list_food[row], minerals=list_minerals[col], value=value_mineral[i]
                )
            )
            i += 1
    # PrincipalNutriments
    principal_nutriments = df.iloc[:, 6:12]
    list_principal = [
        PrincipalNutriments.objects.create(name=principal_name)
        for principal_name in principal_nutriments
    ]
    #"SE CREA LA LISTA DE OBJETOS PRINCIPAL_NUTRIMENTS Y SE LLENA LA BD
    # Value_PrincipalNutriments
    value_nutriments = principal_nutriments.stack()  # transforma los datos en serie
    value_nutrimen = []  # aqui guardaremos los valores de vitaminas del df
    for val in value_nutriments:
        value_nutrimen.append(val)
    i = 0
    list_value_nutriments = []
    for row in range(df.shape[0]):
        for col in range(len(list_principal)):
            list_value_nutriments.append(
                Value_PrincipalNutriments.objects.create(
                    food=list_food[row],
                    principalnutriments=list_principal[col],
                    value=value_nutrimen[i],
                )
            )
            i += 1