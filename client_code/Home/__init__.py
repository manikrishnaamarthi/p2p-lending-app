from ._anvil_designer import HomeTemplate
from anvil import *

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_7_click(self, **event_args):
    open_form('ABOUT')

  def link_1_click(self, **event_args):
    open_form('ONLINECHAT')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('FEEDBACK')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('FAQS')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('BORROW')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('INVEST')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('LOGIN')








  