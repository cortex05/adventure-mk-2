from typing import TypedDict

class KeyItem:
	name: str
	description: str
	display: bool

	def __init__(self, name, description, display):
		self.name = name
		self.description = description
		self.display = display