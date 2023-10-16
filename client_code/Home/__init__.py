from ._anvil_designer import HomeTemplate
from anvil import *

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def link_1_click(self, **event_args):
    open_form('ABOUTUS')

  def link_2_click(self, **event_args):
    open_form('BORROW')

