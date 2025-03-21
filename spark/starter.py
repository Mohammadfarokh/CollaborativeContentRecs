import os

try:
    from pyspark.sql import SparkSession  # noqa: F401
except ImportError:
    pass  # skip this import if we are in pure python environment

def start_spark(
    app_name="Sample",
    url="local[*]",
    memory="10g",
    config=None,
    packages=None,
    jars=None,
    repositories=None,
):

    submit_args = ""
    if packages is not None:
        submit_args = "--packages {} ".format(",".join(packages))
    if jars is not None:
        submit_args += "--jars {} ".format(",".join(jars))
    if repositories is not None:
        submit_args += "--repositories {}".format(",".join(repositories))
    if submit_args:
        os.environ["PYSPARK_SUBMIT_ARGS"] = "{} pyspark-shell".format(submit_args)

    spark_opts = [
        'SparkSession.builder.appName("{}")'.format(app_name),
        'master("{}")'.format(url),
    ]

    if config is not None:
        for key, raw_value in config.items():
            value = (
                '"{}"'.format(raw_value) if isinstance(raw_value, str) else raw_value
            )
            spark_opts.append('config("{key}", {value})'.format(key=key, value=value))

    if config is None or "spark.driver.memory" not in config:
        spark_opts.append('config("spark.driver.memory", "{}")'.format(memory))

    # Set larger stack size
    spark_opts.append('config("spark.executor.extraJavaOptions", "-Xss4m")')
    spark_opts.append('config("spark.driver.extraJavaOptions", "-Xss4m")')

    spark_opts.append("getOrCreate()")
    return eval(".".join(spark_opts))
