from boto3 import Session


def aws_sesion():
    session = Session(
        aws_acces_key_id="xxxxxx",
        aws_secret_acces_key="xxxxx",
        region_name="eu-central-1"
        )

    return session