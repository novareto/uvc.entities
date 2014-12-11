# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute


class IManagers(Interface):
    """
    """
    IPageTop = Attribute("")
    ITabs = Attribute("")
    IAboveContent = Attribute("")
    IBelowContent = Attribute("")
    IHeaders = Attribute("")
    IToolbar = Attribute("")
    IFooter = Attribute("")
    IExtraInfo = Attribute("")


class IMenus(Interface):
    """
    """
    IMenu = Attribute("")
    IGlobalMenu = Attribute("")
    INavigationMenu = Attribute("")
    IPersonalPreferences = Attribute("")
    IFooterMenu = Attribute("")
    IDocumentActions = Attribute("")
    IAddMenu = Attribute("")
    IExtraViews = Attribute("")
    IPersonalMenu = Attribute("")
    IContextualActionsMenu = Attribute("")
    IUserMenu = Attribute("")
    ISubMenu = Attribute("")

   
from .managers import *
from .menus import *
    

class IBrowserEntities(IManagers, IMenus):
    """
    """


__all__ = list(IBrowserEntities) + ['IManagers', 'IMenus', 'IBrowserEntities']
