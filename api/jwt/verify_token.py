from typing import Dict
import jwt
from api.settings import AUTHZ_ISSUER, AUTHZ_AUDIENCE

def verify_token(token: str) -> Dict | None:
    """
    Verify if JWT Token is valid

    Args:
        token (string): raw token

    Returns:
        Dict | None: all properties into token or none if token is invalid
    """
    try:
        # Create a client to access issuer
        jwks_client = jwt.PyJWKClient(AUTHZ_ISSUER+'.well-known/jwks.json')

        # Get Token Headers without verify
        token_header = jwt.get_unverified_header(token)

        # Extract Token key
        key = jwks_client.get_signing_key(token_header["kid"]).key

        # Decode Token
        return jwt.decode(
            token,
            key,
            [token_header["alg"]],
            audience=AUTHZ_AUDIENCE,
            issuer=AUTHZ_ISSUER
        )
    except:
        return None
