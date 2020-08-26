def llenar_tablas_valores(
    df, col_i, col_f, table_name, value_table_name, raw_name, list_food
):
    """
    df: objeto tipo dataframe
    col_i: integer que señala el inicio de las columnas a usar del df
    col_f: final de columnas del df
    table_name: object tipo model, simboliza las tablas en la base de datos
    value_table_name: objeto tipo model que referencia a la tabla de valores
    raw_name: nombre que recibe la tabla, solo es para una vizualizacion, no afecta
    list_food: lista con los objetos tipo model de la tabla FOOD
    """
    print(f"Se comienza a crear la tabla {raw_name}\n")
    table_df = df.iloc[:, col_i:col_f]
    list_nutr_name = [
        table_name.objects.create(name=nutr_name) for nutr_name in table_df
    ]
    print(f"SE CREA LA LISTA DE OBJETOS {raw_name} Y SE LLENA TABLA EN BD\n")

    print(
        f"Se comienza a crear la tabla de valores asociada a las tablas FOOD y {raw_name}"
    )

    value_table = table_df.stack()  # transforma los datos en serie
    values_list = []  # aqui guardaremos los valores del df

    for val in value_table:
        values_list.append(val)

    i = 0
    list_nutr_value = []  # se guardan objetos

    for row in range(df.shape[0]):

        for col in range(len(list_nutr_name)):
            list_nutr_value.append(
                value_table_name.objects.create(
                    food=list_food[row], fk=list_nutr_name[col], value=values_list[i]
                )
            )
            i += 1

    print(f"SE CREA LA LISTA DE OBJETOS VALUE_{raw_name} Y SE LLENA LA BD\n")


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

    path = "food_248.csv"
    df = pd.read_csv(path)

    # Group
    groups = df.FoodGroup.unique()
    list_group = [Group.objects.create(name=group_name) for group_name in groups]
    print("Se crea lista de objetos Group Y SE LLENA EN LA BD")

    # Food
    fk_group = []  # Se almacena el indice del grupo
    number_rows = df.shape[0]

    for item_number in range(number_rows):
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
                group=list_group[fk_group[row]],
            )
        )
    print("SE CREA LA LISTA DE OBJETOS FOOD Y SE LLENA EN LA BD\n")

    # Vitamins y values
    llenar_tablas_valores(df, 12, 21, Vitamins, Value_Vitamins, "VITAMINS", list_food)

    # Minerals value_minerals
    llenar_tablas_valores(
        df, 21, df.shape[1], Minerals, Value_Minerals, "MINERALS", list_food
    )

    # PrincipalNutriments y values
    llenar_tablas_valores(
        df,
        6,
        12,
        PrincipalNutriments,
        Value_PrincipalNutriments,
        "PRINCIPALNUTRIMENTS",
        list_food,
    )

    print("SE HA LLENADO LA BASE DE DATOS\n")
