import jwt

from user.models import UserORM
from ninja.errors import HttpError
from ninja.security import HttpBearer

from api.settings import AUTHZ_ISSUER, AUTHZ_AUDIENCE


class AuthPermission(HttpBearer):
    def authenticate(self, request, token):
        """
        Checks user Autorization token
        """
        #try:
        jwks_client = jwt.PyJWKClient(f'{AUTHZ_ISSUER}.well-known/jwks.json')

        # Get Token Headers without verify
        token_header = jwt.get_unverified_header(token)

        # Extract Token key
        key = jwks_client.get_signing_key(token_header['kid']).key

        # Decode Token
        authz_user = jwt.decode(
            token,
            key,
            [token_header['alg']],
            audience=AUTHZ_AUDIENCE,
            issuer=AUTHZ_ISSUER,
        )
        
        try:
            user = UserORM.objects.get(authz_sub=authz_user['sub'])
        except UserORM.DoesNotExist as err:
            raise HttpError(401, "unauthorized") from err
                
        request.auth = user
        request.permission = authz_user['permissions']
        
        return authz_user
