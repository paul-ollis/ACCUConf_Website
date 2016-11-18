from sqlalchemy import MetaData, Table, select


def query(engine):
    user_infos = Table('user_infos', MetaData(), autoload=True, autoload_with=engine)
    return select([user_infos.c.user_id, user_infos.c.first_name, user_infos.c.last_name]).where(user_infos.c.user_id == 'russel@winder.org.uk')
