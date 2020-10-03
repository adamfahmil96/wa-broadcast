from enum import Enum

class IsEnum(Enum):
    Y = 'Y'
    N = 'N'

class ContentType(Enum):
    TEXT        = 'Text'
    IMAGE       = 'Image'
    VIDEO       = 'Video'
    CONTACT     = 'Contact'
    DOCUMENT    = 'Document'