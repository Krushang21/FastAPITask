from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_user: str
    mysql_pass: str
    mysql_host: str
    mysql_port: int
    mysql_db: str
    model_config = SettingsConfigDict(env_file=".env")

    # jwt_secret_key: str
    # token_expiry_time: int
    # algorithm: str
    # aws_ses_region: str
    # aws_ses_access_key_id: str
    # aws_ses_secret_access_key_id: str
    # source_email: str
    # set_password_email_subject: str
    # jwt_register_expire_time: int
    # send_email_url: str
    # apikey_encryption_key: str
    # free_plan_id: int
