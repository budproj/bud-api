from user.models import UserORM

from user.domain.entities import User

def map_user_orm_to_entity(us_orm: UserORM) -> User:
    return User(
        id=str(us_orm.id),
        authzSub=us_orm.authz_sub,
        role=us_orm.role,
        picture=us_orm.picture,
        gender=us_orm.gender,
        firstName=us_orm.first_name,
        lastName=us_orm.last_name,
        nickname=us_orm.nickname,
        linked_in_profile_address=us_orm.linked_in_profile_address,
        about=us_orm.about,
        email=us_orm.email,
        status=us_orm.status,
        createdAt=us_orm.created_at,
        updatedAt=us_orm.updated_at,
        deletedAt=us_orm.deleted_at
    )