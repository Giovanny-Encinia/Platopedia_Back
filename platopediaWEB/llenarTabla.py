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

    # Food
    fk_group = []  # Se almacena el indice del grupo

    for item_number in range(df.shape[0]):
        group_item = df.FoodGroup.iloc[item_number]
        fk_group.append(
            np.where(groups == group_item)[0][0]
        )  # identifica el indice del grupo

    df_food = df.iloc[:, 2:6]  # Toma las columnas de Food
    r, c = df_food.shape
    rows, cols = np.arange(r), np.arange(c)
    list_food = []  # Se guardaran los objetos de la tabla food

    for row in rows:  # Llena la tabla Food
        list_food.append(
            Food.objects.create(
                description=df_food.iloc[row, 0],
                common_name=df_food.iloc[row, 1],
                brand=df_food.iloc[row, 2],
                scientificname=df_food.iloc[row, 3],
                group=fk_group[row],
            )
        )

    # Vitamins
    vitamins = df.iloc[0:1, 12:21].columns
    list_vitamins = [
        Vitamins.objects.create(name=vitamin_name) for vitamin_name in vitamins
    ]

    # Minerals
    minerals = df.iloc[0:1, 21:]
    list_minerals = [
        Minerals.objects.create(name=mineral_name) for mineral_name in minerals
    ]

    # PrincipalNutriments
    principal_nutriments = df.iloc[0:1, 6:12].columns
    list_principal = [
        PrincipalNutriments.objects.create(name=principal_name)
        for principal_name in principal_nutriments
    ]

    print("Se lleno la tabla")
