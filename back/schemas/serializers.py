def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "login": user["login"],
        "password": user["password"],
        "projects": projects_serializer(user['projects'])
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]


def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "login": user["login"],
        "projects": projects_serializer(user['projects'])
    }


def project_serializer(project) -> dict:
    return {
        "index": str(project["index"]),
        "title": project["title"],
        "imagePath": project["imagePath"],
        "url_project": project["url_project"]
    }


def projects_serializer(projects) -> list:
    return [project_serializer(project) for project in projects]
