from api.application.types import Resource, Command, Scope, Effect, SCOPE_PRIORITY
from user.domain.entities import AuthzData


class PolicyAdapter:
    resources = [
        Resource.PERMISSION,
        Resource.USER,
        Resource.TEAM,
        Resource.CYCLE,
        Resource.FLAGS,
        Resource.OBJECTIVE,
        Resource.KEY_RESULT,
        Resource.KEY_RESULT_CHECK_IN,
        Resource.KEY_RESULT_COMMENT,
        Resource.WORKSPACE,
        Resource.USER_TASK,
    ]

    @staticmethod
    def cut_permission_upper(permission: str) -> str:
        """
        Cuts lower section of permission.
        'team:create:any' -> 'team:create'
        """
        return permission.split(':').pop().join(':')
    
    @staticmethod
    def build_action(resource: Resource, command: Command) -> str:
        """
        Build a action(Resource:Command) using enum values.
        """
        return f'{resource}:{command}'
    
    @staticmethod
    def user_has_permission(user: AuthzData, permission: str) -> bool:
        """
        Check if user has a permission.
        """
        return permission in user.permissions

    @staticmethod
    def build_permission_from_action(action: str, scope: Scope) -> str:
        """
        Build a permission using an action as base.
        """
        return f'{action}:{scope}'
    
    @staticmethod
    def build_permission(resource: Resource, command: Command, scope: Scope) -> str:
        return f'{resource}:{command}:{scope}'
    
    def get_resource_policy_from_permissions(self, permissions: list[str], resources: list[Resource] = resources):
        commandPolicies = [self.get_command_policies_for_resource_from_permissions(resource, permissions) for resource in resources]
        return {key: value for key, value in zip(resources, commandPolicies)}
    
    def get_command_policies_for_resource_from_permissions(self, resource: Resource, permissions: list[str]):
        commands = [i.value for i in Command]
        scopePolicies = [self.get_scope_policies_for_resource_command_from_permissions(resource, command, permissions) for command in commands]
        return {key: value for key, value in zip(commands, scopePolicies)}
    
    def get_scope_policies_for_resource_command_from_permissions(self, resource: Resource, command: str, permissions: list[str]):
        action = f'{resource}:{command}'
        actionPermissions = self.filter_action_permissions_from_permissions(action, permissions)
        scopes = [i.value for i in Scope]
        effectPolicies = [self.get_effect_policy_for_action_scope_from_permissions(scope, action, actionPermissions) for scope in scopes]
        return {key: value for key, value in zip(scopes, effectPolicies)}

    def filter_action_permissions_from_permissions(self, action: str, permissions: list[str]):
        return [permission for permission in permissions if action in permission]

    def get_effect_policy_for_action_scope_from_permissions(self, scope: str, action: str, permissions: list[str]) -> Effect:
        expectedPermission = f'{action}:{scope}'
        return Effect.ALLOW if expectedPermission in permissions else Effect.DENY

    def get_resource_command_scope_for_user(self, resource: Resource, command: Command, user: AuthzData) -> Scope:
        action = self.build_action(resource, command)
        return self.get_highest_scope_for_action_from_user(action, user)
    
    
    def get_highest_scope_for_action_from_user(self, action: str, user: AuthzData) -> Scope:
        for scope in SCOPE_PRIORITY:
            permission = self.build_permission_from_action(action, scope)
            if self.user_has_permission(user, permission):
                return scope
        return Scope.OWNS

    # def getResourcesCommandStatementsForScopeFromPolicy(self, policy, scope: Scope): ResourceStatement<CommandStatement> {
    #    return mapValues(policy, (commandPolicy) =>
    #    this.getCommandStatementsForScopeFromPolicy(commandPolicy, scope),