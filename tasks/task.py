import pandas as pd

import openpyxl

from app import database as db

from app.models import User, Unit, Employment
import datetime
from dateutil import parser
 

import pandas as pd

import openpyxl

from app import database as db

from app.models import User, Unit, Employment
import datetime
from dateutil import parser


class DatabaseExecutor:

	def __init__(self, session = db.session):

			self.session = db.session

	def get_or_create(self, model, uniquefield, defaults=None, **kwargs):

		instance = self.session.query(model).filter_by(**uniquefield).one_or_none()

		if instance:
			return instance, False

		kwargs |= defaults or {}
		kwargs |= uniquefield

		instance = model(**kwargs)

		try:
			self.session.add(instance)
			self.session.commit()
		except Exception as error:
			print(error) 
			self.session.rollback()
			instance = self.session.query(model).filter_by(**uniquefield).one()
			return instance, False
		else:
			return instance, True

	def create_or_update(self, model, uniquefield, **kwargs):

		instance = self.session.query(model).filter_by(**uniquefield).one_or_none()

		if not instance:

			kwargs |= uniquefield

			instance = model(**kwargs)
			self.session.add(instance)
			
		else:

			for key, value in kwargs.items():

				setattr(instance, key, value)

		self.session.commit()

	def flush_tables_rows(self, meta = db.metadata):

		meta = db.metadata

		for table in reversed(meta.sorted_tables):

			self.session.execute(table.delete())

		self.session.commit()

class ExcelExecutor:

	def __init__(self, filepath:str = None, db_executor = DatabaseExecutor()):

		self.filepath = filepath

		self.db_executor = db_executor

		df = pd.DataFrame()

		if self.filepath:

			self.load(filepath)

	def read_flat(self) -> dict:

		return self.df

	# def save_to_db(self, )

	def save_to_db(self, df = None):

		df = df or self.df

		for _, row in df.iterrows():

			user, created_user = self.db_executor.get_or_create(User, {'name' : row['Name']}, salary = 30)
			unit, created_unit = self.db_executor.get_or_create(Unit, {'name' : row['Unit']})

			self.db_executor.create_or_update(Employment, {'user_id' : user.id, 'unit_id' : unit.id}, years_active = row['Tenure (Years)'])


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

	def save_users_from_csv(self, path = 'base_users.csv'):

		df = pd.read_csv(path)

		for _, row in df.iterrows():

			print(*row['time_created'].strip().split('/'))

			self.db_executor.create_or_update(User, {'name': row['name']}, salary = row['salary'], 
				time_created = parser.parse(row['time_created']))





if __name__ == '__main__':

	from pathlib import Path

	BASE_DIR = Path(__file__).resolve().parent.parent

	ex = ExcelExecutor(f'{BASE_DIR}/user_unit_tenure.xlsx')