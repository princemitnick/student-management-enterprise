from fastapi.security import OAuth2PasswordRequestForm

def get_token(form: OAuth2PasswordRequestForm) -> str:
    return form.username