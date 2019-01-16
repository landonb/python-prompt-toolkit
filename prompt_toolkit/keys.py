from __future__ import unicode_literals

__all__ = [
    'Keys',
    'ALL_KEYS',
]


class Keys(object):
    """
    List of keys for use in key bindings.
    """
    Escape = 'escape'  # Also Control-[

    ControlAt = 'c-@'  # Also Control-Space.

    ControlA = 'c-a'
    ControlB = 'c-b'
    ControlC = 'c-c'
    ControlD = 'c-d'
    ControlE = 'c-e'
    ControlF = 'c-f'
    ControlG = 'c-g'
    ControlH = 'c-h'
    ControlI = 'c-i'  # Tab
    ControlJ = 'c-j'  # Newline
    ControlK = 'c-k'
    ControlL = 'c-l'
    ControlM = 'c-m'  # Carriage return
    ControlN = 'c-n'
    ControlO = 'c-o'
    ControlP = 'c-p'
    ControlQ = 'c-q'
    ControlR = 'c-r'
    ControlS = 'c-s'
    ControlT = 'c-t'
    ControlU = 'c-u'
    ControlV = 'c-v'
    ControlW = 'c-w'
    ControlX = 'c-x'
    ControlY = 'c-y'
    ControlZ = 'c-z'

    MetaA = 'm-a'
    MetaB = 'm-b'
    MetaC = 'm-c'
    MetaD = 'm-d'
    MetaE = 'm-e'
    MetaF = 'm-f'
    MetaG = 'm-g'
    MetaH = 'm-h'
    MetaI = 'm-i'
    MetaJ = 'm-j'
    MetaK = 'm-k'
    MetaL = 'm-l'
    MetaM = 'm-m'
    MetaN = 'm-n'
    MetaO = 'm-o'
    MetaP = 'm-p'
    MetaQ = 'm-q'
    MetaR = 'm-r'
    MetaS = 'm-s'
    MetaT = 'm-t'
    MetaU = 'm-u'
    MetaV = 'm-v'
    MetaW = 'm-w'
    MetaX = 'm-x'
    MetaY = 'm-y'
    MetaZ = 'm-z'

    Meta1 = 'm-1'
    Meta2 = 'm-2'
    Meta3 = 'm-3'
    Meta4 = 'm-4'
    Meta5 = 'm-5'
    Meta6 = 'm-6'
    Meta7 = 'm-7'
    Meta8 = 'm-8'
    Meta9 = 'm-9'
    Meta0 = 'm-0'
    MetaMinus = 'm--'
    MetaEquals = 'm-='
    # Keys in shift position of number keys (on US English keyboard):
    MetaExclamation = 'm-!'
    MetaAt = 'm-@'
    MetaPound = 'm-#'
    MetaDollar = 'm-$'
    MetaPercent = 'm-%'
    MetaCaret = 'm-^'
    MetaAmpersand = 'm-&'
    MetaAsterisk = 'm-*'
    MetaLeftParenthesis = 'm-('
    MetaRightParenthesis = 'm-)'
    MetaUnderscore = 'm-_'
    MetaPlus = 'm-+'
    # Same as last group, but the achieved the long way:
    MetaShift1 = 'm-s-1'
    MetaShift2 = 'm-s-2'
    MetaShift3 = 'm-s-3'
    MetaShift4 = 'm-s-4'
    MetaShift5 = 'm-s-5'
    MetaShift6 = 'm-s-6'
    MetaShift7 = 'm-s-7'
    MetaShift8 = 'm-s-8'
    MetaShift9 = 'm-s-9'
    MetaShift0 = 'm-s-0'
    MetaShiftMinus = 'm-s--'
    MetaShiftEquals = 'm-s-='

    ControlBackslash   = 'c-\\'
    ControlSquareClose = 'c-]'
    ControlCircumflex  = 'c-^'
    ControlUnderscore  = 'c-_'

    ControlLeft        = 'c-left'
    ControlRight       = 'c-right'
    ControlUp          = 'c-up'
    ControlDown        = 'c-down'

    ControlShiftLeft   = 'c-s-left'
    ControlShiftRight  = 'c-s-right'
    ControlShiftUp     = 'c-s-up'
    ControlShiftDown   = 'c-s-down'

    Up          = 'up'
    Down        = 'down'
    Right       = 'right'
    Left        = 'left'

    ShiftLeft   = 's-left'
    ShiftUp     = 's-up'
    ShiftDown   = 's-down'
    ShiftRight  = 's-right'
    ShiftDelete = 's-delete'
    BackTab     = 's-tab'  # shift + tab

    Home        = 'home'
    End         = 'end'
    Delete      = 'delete'
    ControlDelete = 'c-delete'
    PageUp      = 'pageup'
    PageDown    = 'pagedown'
    Insert      = 'insert'

    F1 = 'f1'
    F2 = 'f2'
    F3 = 'f3'
    F4 = 'f4'
    F5 = 'f5'
    F6 = 'f6'
    F7 = 'f7'
    F8 = 'f8'
    F9 = 'f9'
    F10 = 'f10'
    F11 = 'f11'
    F12 = 'f12'
    F13 = 'f13'
    F14 = 'f14'
    F15 = 'f15'
    F16 = 'f16'
    F17 = 'f17'
    F18 = 'f18'
    F19 = 'f19'
    F20 = 'f20'
    F21 = 'f21'
    F22 = 'f22'
    F23 = 'f23'
    F24 = 'f24'

    ControlF1 = 'c-f1'
    ControlF2 = 'c-f2'
    ControlF3 = 'c-f3'
    ControlF4 = 'c-f4'
    ControlF5 = 'c-f5'
    ControlF6 = 'c-f6'
    ControlF7 = 'c-f7'
    ControlF8 = 'c-f8'
    ControlF9 = 'c-f9'
    ControlF10 = 'c-f10'
    ControlF11 = 'c-f11'
    ControlF12 = 'c-f12'

    # Matches any key.
    Any = '<any>'

    # Special.
    ScrollUp    = '<scroll-up>'
    ScrollDown  = '<scroll-down>'

    CPRResponse = '<cursor-position-response>'
    Vt100MouseEvent = '<vt100-mouse-event>'
    WindowsMouseEvent = '<windows-mouse-event>'
    BracketedPaste = '<bracketed-paste>'

    # For internal use: key which is ignored.
    # (The key binding for this key should not do anything.)
    Ignore = '<ignore>'


ALL_KEYS = [getattr(Keys, k) for k in dir(Keys) if not k.startswith('_')]


# Aliases.
KEY_ALIASES = {
    'backspace': 'c-h',
    'c-space': 'c-@',
    'enter': 'c-m',
    'tab': 'c-i',
}


# The following should not end up in ALL_KEYS, but we still want them in Keys
# for backwards-compatibility.
Keys.ControlSpace = Keys.ControlAt
Keys.Tab          = Keys.ControlI
Keys.Enter        = Keys.ControlM
Keys.Backspace    = Keys.ControlH
