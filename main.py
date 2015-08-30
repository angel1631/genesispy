from core.librerias.propias.py.base import DataBase
from core.modulos.category.driver import DriverCategory
valores = {'acc': '1', 'values':{'id': '', 'titulo': 'Computadoras', 'padre': '1', 'estatus': '1'}}
driver = DriverCategory(valores)
driver.execute_action()