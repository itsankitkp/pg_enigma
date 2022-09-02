import psycopg2
class PostgresConf:
    
    def __init__(self, connect_str: str='dbname=testdb host=localhost user=testrole password=testpwd') -> None:
        self.conn = psycopg2.connect(connect_str)
        
    def set_work_mem(self, amt):
        cur = self.conn.cursor()
        cur.execute(f"SET work_mem = '{amt}MB'")
        cur.close()
        