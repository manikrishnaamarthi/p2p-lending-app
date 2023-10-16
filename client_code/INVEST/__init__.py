from ._anvil_designer import INVESTTemplate
from anvil import *

class INVEST(INVESTTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
