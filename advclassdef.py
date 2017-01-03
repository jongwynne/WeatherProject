class Product(object):

    """base object for new products in adventureworks"""
    def __init__(self):
        import pyodbc
        self.cnxn = pyodbc.connect('DSN=KubrickSQLServer')

    def add_product(self, cd, nm, lp, cs):
        self.prodcode = cd
        self.name = nm
        self.listprice = lp
        self.cost = cs
        cursor = self.cnxn.cursor()
        cursor.execute("""
        insert into dbo.products
        (productcode, productname, price, cost)
        Values (?,?,?,?)
        """, self.prodcode, self.name, self.listprice, self.cost)
        self.cnxn.commit()

    def remove_product(self, cd):
        self.prodcode = cd
        cursor = self.cnxn.cursor()
        cursor.execute("""
        delete from dbo.products
        where productcode = ?
        """, self.prodcode)
        self.cnxn.commit()

    def query_product(self):
        cursor = self.cnxn.cursor()
        cursor.execute("""
        select * from dbo.products
        where productcode = ?
        """, self.prodcode)
        self.cnxn.commit()
