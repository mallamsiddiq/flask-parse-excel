import pandas as pd

import openpyxl

from app import database as db

from app.models import User, Unit, Employment
import datetime
from dateutil import parser
 




def get_or_create(session, model, uniquefield, defaults=None, **kwargs):


	instance = session.query(model).filter_by(**uniquefield).one_or_none()

	if instance:
		return instance, False

	kwargs |= defaults or {}
	kwargs |= uniquefield

	instance = model(**kwargs)

	try:
		session.add(instance)
		session.commit()
	except Exception as error:
		print(error) 
		session.rollback()
		instance = session.query(model).filter_by(**uniquefield).one()
		return instance, False
	else:
		return instance, True

def create_or_update(session, model, uniquefield, **kwargs):

	instance = session.query(model).filter_by(**uniquefield).one_or_none()

	if not instance:

		kwargs |= uniquefield

		instance = model(**kwargs)
		session.add(instance)
		
	else:

		for key, value in kwargs.items():

			setattr(instance, key, value)

	session.commit()

def save_users_from_csv(path: str) -> None:

	df = pd.read_csv(path)

	for _, row in df.iterrows():

		create_or_update(db.session, User, {'name': row['name']}, salary = row['salary'], 
			time_created = parser.parse(row['time_created']))


class ExcelExecutor:

	def __init__(self, filepath:str = None):

		self.filepath = filepath

		df = pd.DataFrame()

		if self.filepath:

			self.load(filepath)

	def read_flat(self) -> dict:

		return self.df

	# def save_to_db(self, )

	def save_to_db(self, df = None):

		df = df or self.df

		for _, row in df.iterrows():

			user, created_user = get_or_create(db.session, User, {'name' : row['Name']}, salary = 30)
			unit, created_unit = get_or_create(db.session, Unit, {'name' : row['Unit']})


			employment = Employment(user_id = user.id,
									unit_id = unit.id,
									years_active = row['Tenure (Years)'])

			
			user.units_rel.append(employment)

			db.session.commit()


	def read_grouped_on_name(self):

		df = self.df

		names = df.Name.unique()

		gf = df.groupby('Name')


		for name in gf.groups:

			yield({'name': name, 'obj' : (gf.get_group(name)[['Unit', 'Tenure (Years)']].reset_index(drop=True)).to_html()})




	def load(self, path: str) -> dict:

		self.df = pd.read_excel(path)

		df = self.df

		return




if __name__ == '__main__':

	from pathlib import Path

	BASE_DIR = Path(__file__).resolve().parent.parent

	ex = ExcelExecutor(f'{BASE_DIR}/user_unit_tenure.xlsx')
	