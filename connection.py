import mysqi.connector as connector
from mysqi.connector import Error

try{
    conncetion = connector.connect(
        host: "localhost",
        password: "hello",
        port: 3306,
        user: 'root',
        database: 'tutorial'
    )
}
except Error as e:
    print('could not connect to database', e)