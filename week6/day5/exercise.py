class MenuItem:
    cursor = ''
    connection = ''

    def __init__(self, title, price, connection) -> None:
        self.title = title
        self.price = price
        MenuItem.connection = connection
        MenuItem.cursor = connection.cursor()
    
    def __repr__(self):
        return f'{self.title} {self.price}'

    def save(self):
        MenuItem.cursor.execute(
            f'INSERT INTO menu_items (title ,price) VALUES (\'{self.title}\', \'{self.price}\')'
        )
        MenuItem.connection.commit()
        print(f'{self.title} {self.price} was added successfully.')

    def delete(self):
        MenuItem.cursor.execute(
            f'delete from menu_items where title = \'{self.title}\''
        )
        MenuItem.connection.commit()
        print(f'deleted {self.title} successfully')

    def update(self, title, price):
        MenuItem.cursor.execute(
            f'update menu_items set title = \'{title}\', price = \'{price}\' where title = \'{self.title}\''
        )
        MenuItem.connection.commit()
        print(f'updated to {title} {price} successfully')

    def all(connection):
        cursor = connection.cursor()
        cursor.execute(f'select * from menu_items')
        objects_raw = cursor.fetchall()
        objects = [MenuItem(x[1], x[2], connection) for x in objects_raw]
        for obj in objects:
            print(obj)
        return objects

    def get_by_name(title, connection):
        cursor = connection.cursor()
        cursor.execute(
            f'select * from menu_items where title = \'{title}\'')
        obj = cursor.fetchone()
        if obj is None:
            return None
        return MenuItem(obj[1], float(obj[2]), connection)
