import dlt

@dlt.table
def transforrmed():
    return spark.range(10)
