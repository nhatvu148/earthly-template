import polars as pl
import numpy as np


def run_polars():
    pl.Config.set_tbl_cols(50)
    pl.Config.set_tbl_rows(600)
    pl.Config.set_fmt_str_lengths(100)

    csv_file = "data/titanic.csv"

    df = pl.read_csv(csv_file)

    print(df)
    # print(df.head(3))
    # print(df.glimpse())

    # Expressions
    # print(df[:5, ["Pclass", "Name", "Age"]])

    # Expression API
    # An expression is a function that takes a Series (or column in a DataFrame) in and returns Series (or column in a DataFrame).
    # print(df
    #       .select(
    #           [
    #               pl.col("Pclass"),
    #               pl.col("Name"),
    #               pl.col("Age"),
    #           ]
    #       ))

    # print(df
    #       .select(
    #           [
    #               # Identity expression
    #               pl.col("Pclass"),
    #               # Names to lowercase
    #               pl.col("Name").str.to_lowercase(),
    #               # Round the ages
    #               pl.col("Age").round(2)
    #           ]
    #       ))

    # print(df
    #       .select(
    #           [
    #               # Get the Name column without changes
    #               pl.col("Name"),
    #               # Take the Name column and split it into a list of separate words
    #               pl.col("Name").str.split(" ").alias("Name_split"),
    #               # Take the Name column, split it into a list of separate words and
    #               # count the number of words
    #               pl.col("Name").str.split(
    #                   " ").list.len().alias("Name_word_count"),
    #           ]
    #       ))

    # print((
    #     df
    #     .select(
    #         pl.col(pl.INTEGER_DTYPES)
    #     )
    #     .head(3)
    # ))

    # print(df
    #       .filter(
    #           pl.col("Age") > 70
    #       ))

    # print(df.describe())
    # print(df["Pclass"].value_counts())
    # print(df
    #       .group_by(["Survived", "Pclass"])
    #       .agg(
    #           pl.col("PassengerId").count().alias("counts")
    #       ))

    # print(df
    #       .with_columns(
    #           pl.col("Age").max().over("Pclass").alias("MaxAge")
    #       )
    #       .select("Pclass", "Age", "MaxAge")
    #       .head(3))

    # Lazy mode
    print(pl.scan_csv(csv_file)
          .group_by(["Survived", "Pclass"])
          .agg(
        pl.col("PassengerId").count().alias("counts")
    ))
    print(
        pl.scan_csv(csv_file)
        .group_by(["Survived", "Pclass"])
        .agg(
            pl.col("PassengerId").count().alias("counts")
        )
        .explain()
    )

    print(
        pl.scan_csv(csv_file)
        .filter(pl.col("Age") > 50)
        .group_by(["Survived", "Pclass"])
        .agg(
            pl.col("PassengerId").count().alias("counts")
        )
        .explain()
    )

    # Query evaluation
    df_lazy = pl.scan_csv(csv_file)
    print(
        df_lazy
        .filter(pl.col("Age") > 50)
        .group_by(["Survived", "Pclass"])
        .agg(
            pl.col("PassengerId").count().alias("counts")
        )
        .collect()
    )

    # print(df_lazy.collect_schema())
    # print(
    #     df_lazy
    #     .select(
    #         pl.len()
    #     )
    #     .collect()
    # )

    # A method on a DataFrame acts on the data. An method on a LazyFrame acts
    # on the query plan.
    pl.LazyFrame({"values": [0, 1, 2]})
    pl.DataFrame({"values": [0, 1, 2]}).lazy()

    print(
        pl.scan_csv(csv_file)
        .select(
            (pl.col("Age").mean() - pl.col("Age").std()).alias("minus_one_std"),
            pl.col("Age").mean().alias("mean"),
            (pl.col("Age").mean() + pl.col("Age").std()).alias("plus_one_std"),
        )
        .collect()
    )

    print(
        pl.scan_csv(csv_file)
        .select(
            (pl.col("Age").mean() - pl.col("Age").std()).alias("minus_one_std"),
            pl.col("Age").mean().alias("mean"),
            (pl.col("Age").mean() + pl.col("Age").std()).alias("minus_one_std"),
        )
        .explain()
    )

    # Streaming larger-than-memory datasets
    # print(
    #     df_lazy
    #     .filter(pl.col("Age") > 50)
    #     .group_by(["Survived", "Pclass"])
    #     .agg(
    #         pl.col("PassengerId").count().alias("counts")
    #     )
    #     .collect(streaming=True)
    # )

    # print(df.to_arrow())
    # print(df["Age"].to_arrow())

    df_shape = (1_000_000, 100)
    df_polars = pl.DataFrame(
        np.random.standard_normal(df_shape)
    )
    print(df_polars.shape)

    return df
