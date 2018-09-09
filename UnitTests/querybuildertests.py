import sys
import unittest

sys.path.append('D:\Workouts\Python\Germaneness\Samples\Example1')

from Database import Query


class TestStringMethods(unittest.TestCase):

    def test_insert_query_built_successful(self):
        key = [{'a': 'a', 'b': 'b'}, {'c': 'c', 'd': 'd'}]
        query_builder = Query('')
        query_builder.insert_multiple('sample', key)
        self.assertEqual("Insert into sample (a, b) values ('a', 'b'), ('c', 'd')", query_builder.query_built)

    def test_normal_select_with_column(self):
        print('test_normal_select_with_column - Begin')
        query = Query('sample-1')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        query.select().columns('a, b, c')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        self.assertEqual("Select a, b, c".upper().strip(), query.query_built.upper().strip())
        print('test_normal_select_with_column - End')

    def test_normal_select_with_condition_simple_where(self):
        print('test_normal_select_with_column_simple_where - Begin')
        query = Query('sample-1')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        query.select().columns('a, b, c').where().condition('a = b')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        self.assertEqual("Select a, b, c where a = b".upper().strip(), query.query_built.upper().strip())
        print('test_normal_select_with_column_simple_where - End')

    def test_normal_select_with_where_condition_value(self):
        print('test_normal_select_with_column_simple_where - Begin')
        query = Query('sample-1')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        query.select().columns('a, b, c').where_column("a").equals().value(10)
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        self.assertEqual("Select a, b, c where a = 10".upper().strip(), query.query_built.upper().strip())
        print('test_normal_select_with_column_simple_where - End')

    def test_normal_select_with_where_condition_As_Null(self):
        print('test_normal_select_with_column_simple_where - Begin')
        query = Query('sample-1')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        query.select().columns('a, b, c').where_null("a")
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        self.assertEqual("Select a, b, c where a is Null".upper().strip(), query.query_built.upper().strip())
        print('test_normal_select_with_column_simple_where - End')

    def test_join_select_Without_Condition(self):
        print('test_normal_select_with_column_Join - Begin')
        query = Query('sample-1')
        print('TableName : {}, Query Built:{}'.format(query.table_name, query.query_built))
        query.select().columns('a.sample-1_2, a.sample-1_3, b.sample-1_2, b.sample-1_4').from_table().alias("a") \
            .join("sample-2", "b").on().join_column("sample-1", "sample-1_2").equals() \
            .join_column("sample-2", "sample-1_2")
        print(query.query_built.upper().strip())
        self.assertEqual("Select a.sample-1_2, a.sample-1_3, b.sample-1_2, b.sample-1_4 From sample-1 as a join "
                         "sample-2 as b on a.sample-1_2 = b.sample-1_2".upper().strip(), query.query_built.upper()
                         .strip())
        print('test_normal_select_with_column_Join - End')

    def test_select_where_column_relates_another_column(self):
        print('test_select_where_column_relates_another_column - Begin')
        query = Query('aSample')
        query.select().from_table().alias('a').join('bSample', 'b').on().join_column('bSample', 'field-1').equals() \
            .join_column('aSample', 'field-1').where_column_relates_another_column('a.field2', ' = ', 'b.field2')
        print(query.query_built)
        self.assertEqual("Select From aSample as a join bSample as b on b.field-1 = a.field-1 where a.field2  =  "
                         "b.field2".upper().strip(), query.query_built.upper().strip())
        print('test_select_where_column_relates_another_column - End')

    def test_select_complex_condition_where(self):
        print('test_select_complex_condition_where - Begin')
        query = Query('aSample').select().from_table().where_column_relates_another_column('field-1', '=', 10) \
            .and_op() \
            .column("field-2").in_op().open_brackets().select().column('id').from_table('bSample').where_column('id') \
            .equals().value(10).close_brackets()
        print(query.query_built)
        self.assertEqual("Select From aSample where field-1 = 10 And field-2 in (Select id From bSample Where id = 10 )"
                         .upper().strip(), query.query_built.upper().strip())
        print('test_select_complex_condition_where - End')

    def test_select_union_query(self):
        print('test_select_union_query - Begin')
        query = Query('Sample-1').select().columns('*').from_table().union().select().columns('*') \
            .from_table('Sample-2')
        print(query.query_built)
        self.assertEqual("Select * From Sample-1 Union Select * From Sample-2".upper().strip(),
                         query.query_built.upper().strip())
        print('test_select_union_query - End')


if __name__ == '__main__':
    unittest.main()
