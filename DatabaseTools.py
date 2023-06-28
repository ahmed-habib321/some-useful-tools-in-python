import mysql.connector
from ttktools import *

__connection = None
__cursor = None


def get_connection():
    """
    Returns the current database connection object.
    """
    return __connection


def get_cursor():
    """
    Returns the current database cursor object.
    """
    return __cursor


def is_connected():
    """
    Checks if a database connection is established.
    """
    return __connection is not None


def create_connection(database_name=""):
    """
    Creates a new database connection.

    Args:
        database_name (str): Name of the database (optional).

    Raises:
        mysql.connector.Error: If an error occurs while creating the connection.
    """
    try:
        global __connection
        global __cursor
        __connection = mysql.connector.connect(user="root", passwd="", database=database_name)
        __cursor = __connection.cursor(buffered=True)
    except mysql.connector.Error as ex:
        msg(ex)


################################################################################################

def create_database(database_name):
    """
    Creates a new database if it doesn't exist.

    Args:
        database_name (str): Name of the database to create.

    Raises:
        mysql.connector.Error: If an error occurs while creating the database.
    """
    try:
        if not is_connected():
            create_connection()
        if is_connected():
            __cursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci".format(
                    database_name
                )
            )
            __connection.commit()
            create_connection(database_name)
    except mysql.connector.Error as ex:
        msg(ex)

def delete_database(database_name):
    """
    Deletes a database.

    Args:
        database_name (str): Name of the database to delete.

    Raises:
        mysql.connector.Error: If an error occurs while deleting the database.
    """
    try:
        if not is_connected():
            create_connection()
        if is_connected():
            __cursor.execute("DROP DATABASE IF EXISTS {}".format(database_name))
            __connection.commit()
    except mysql.connector.Error as ex:
        msg(ex)

def execute(sql):
    """
    Executes an SQL query.

    Args:
        sql (str): SQL query to execute.

    Raises:
        BaseException: If an error occurs while executing the query.
    """
    try:
        if is_connected():
            __cursor.execute(sql)
            __connection.commit()
    except BaseException as ex:
        msg(ex)


def get_data(sql):
    """
    Executes an SQL query and returns the fetched data.

    Args:
        sql (str): SQL query to execute.

    Returns:
        list: Fetched data as a list of tuples.

    Raises:
        BaseException: If an error occurs while executing the query.
    """
    try:
        if is_connected():
            __cursor.execute(sql)
            __connection.commit()
            return __cursor.fetchall()
        else:
            return []
    except BaseException as ex:
        msg(ex)

def get_auto_number(table, column):
    """
    Retrieves the next auto-increment value for a column in a table.

    Args:
        table (str): Name of the table.
        column (str): Name of the auto-increment column.

    Returns:
        int: Next auto-increment value.

    Raises:
        BaseException: If an error occurs while retrieving the value.
    """
    try:
        if is_connected():
            __cursor.execute("SELECT MAX({})+1 FROM {}".format(column, table))
            __connection.commit()
            result = __cursor.fetchone()[0]
            if result is None:
                return 1
            else:
                return result
        else:
            return -1
    except BaseException as ex:
        msg(ex)




            ##########  Custom operations   ##############


def create_table(name, primary_key, data_type, size):
    """
    Creates a new table if it doesn't exist.

    Args:
        name (str): Name of the table.
        primary_key (str): Name of the primary key column.
        data_type (str): Data type of the primary key column.
        size (int): Size of the primary key column.

    Raises:
        BaseException: If an error occurs while creating the table.
    """
    execute(
        """CREATE TABLE IF NOT EXISTS {} ({} {}({}) PRIMARY KEY);""".format(
            name, primary_key, data_type, size
        )
    )

def add_column(table, name, data_type, size):
    """
    Adds a new column to a table.

    Args:
        table (str): Name of the table.
        name (str): Name of the column to add.
        data_type (str): Data type of the column.
        size (int): Size of the column.

    Raises:
        BaseException: If an error occurs while adding the column.
    """
    execute(
        """ALTER TABLE {} ADD IF NOT EXISTS {} {}({})""".format(
            table, name, data_type, size
        )
    )

def delete_column(table, name):
    """
    Deletes a column from a table.

    Args:
        table (str): Name of the table.
        name (str): Name of the column to delete.

    Raises:
        BaseException: If an error occurs while deleting the column.
    """
    execute("""ALTER TABLE {} DROP COLUMN IF EXISTS {}""".format(table, name))


def get_all_table_data(table):
    """
    Retrieves all data from a table.

    Args:
        table (str): Name of the table.

    Returns:
        list: Fetched data as a list of tuples.
    """
    return get_data("SELECT * FROM {}".format(table))


def is_exist(value, primary_key, table):
    """
    Checks if a value exists in a table for a given primary key column.

    Args:
        value: Value to check.
        primary_key (str): Name of the primary key column.
        table (str): Name of the table.

    Returns:
        bool: True if the value exists, False otherwise.
    """
    records = get_data(
        "SELECT * FROM {} WHERE {} = '{}'".format(table, primary_key, str(value))
    )
    return bool(records)

# Usage examples
# create_table("mytable", "id", "INT", 10)
# add_column("mytable", "name", "VARCHAR", 50)
# delete_column("mytable", "name")
# print(get_all_table_data("mytable"))
# print(is_exist("John Doe", "name", "mytable"))