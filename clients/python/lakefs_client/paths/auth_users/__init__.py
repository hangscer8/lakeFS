# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lakefs_client.paths.auth_users import Api

from lakefs_client.paths import PathValues

path = PathValues.AUTH_USERS