# JDBC Format으로 DB의 데이터를 가져올 때, Table의 크기를 적절히 나누어 쿼리하는 기능

spark_jdbc_reader = ... # spark.option

target_table = 'TB_C_PRODUCT'
target_table_index_column = 'C_PRDUCT_NO'
schema = 'bcme'

get_table_min_max_index_query = f"""(
    SELECT
        MIN({target_table_index_column}) AS lowerbound,
        MAX({target_table_index_column}) AS upperbound
    FROM
        {schema}.{target_table}
) AS S"""

bound_option = (spark_jdbc_reader
    .option('dbtable', get_table_min_max_index_query)
    .option('numPartitions', 1)
    .load()
    .first()
)

lower_bound = bound_option['lowerbound']
upper_bound = bound_option['upperbound']

partition_size = 32
spark_df = (spark_jdbc_reader
    .option('dbtable', f'{schema}.{target_table}')
    .option('numPartitions', partition_size)
    .option('lower_bound', lower_bound)
    .option('upper_bound', upper_bound)
    .load()
)