# -*- coding: utf-8 -*-

from dolmen.menu.interfaces import IMenu


class IGlobalMenu(IMenu):
    """Marker for GlobalMenu
    """


class INavigationMenu(IMenu):
    """Marker for NavigationMenu
    """


class IPersonalPreferences(IMenu):
    """Marker for PersonalPreferences
    """


class IQuicklinksMenu(IMenu):
    """Marker for QuicklinksMenu
    """


class IFooterMenu(IMenu):
    """Marker for Footer
    """


class IDocumentActions(IMenu):
    """Marker for DocumentActions
    """

    
class IAddMenu(IMenu):
    """Marker for the Add Menu
    """
    

class IExtraViews(IMenu):
    """Marker for additional Views for Folders
       Objects etc...
    """


class IPersonalMenu(IMenu):
    """Marker for PersonalMenu
    """


class IContextualActionsMenu(IMenu):
    """Marker for PersonalMenu
    """


class IUserMenu(IMenu):
    """Marker for the UserMenu
    """


class ISubMenu(IMenu):
    pass


__all__ = [
    "IMenu",
    "IGlobalMenu",
    "INavigationMenu",
    "IPersonalPreferences",
    "IFooterMenu",
    "IDocumentActions",
    "IAddMenu",
    "IExtraViews",
    "IPersonalMenu",
    "IContextualActionsMenu",
    "IUserMenu",
    "ISubMenu",
    ]
