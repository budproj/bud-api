from enum import Enum


class Resource(Enum):
    PERMISSION = 'permission'
    USER = 'user'
    USER_SETTING = 'user-setting'
    TEAM = 'team'
    FLAGS = 'flags'
    CYCLE = 'cycle'
    OBJECTIVE = 'objective'
    KEY_RESULT = 'key-result'
    KEY_RESULT_SUPPORT_TEAM = 'key-result-support-team'
    KEY_RESULT_CHECK_IN = 'key-result-check-in'
    KEY_RESULT_COMMENT = 'key-result-comment'
    KEY_RESULT_CHECK_MARK = 'key-result-check-mark'
    WORKSPACE = 'workspace'
    USER_TASK = 'user-task'


class Command(Enum):
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    DELETE = 'delete'


class Scope(Enum):
    ANY = 'any'
    COMPANY = 'company'
    TEAM = 'team'
    OWNS = 'owns'

SCOPE_PRIORITY = [Scope.ANY, Scope.COMPANY, Scope.TEAM, Scope.OWNS]
    

class Effect(Enum):
    ALLOW = 'allow'
    DENY = 'deny'