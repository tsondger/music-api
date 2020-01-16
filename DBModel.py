import sqlalchemy as db

engine = db.create_engine(r'sqlite:///chinook.db')
conn = engine.connect()

metadata = db.MetaData()



"""
albums = db.Table('albums', metadata, autoload=True, autoload_with=engine)
tracks = db.Table('tracks', metadata, autoload=True, autoload_with=engine)
genres = db.Table('genres', metadata, autoload=True, autoload_with=engine)

tt = conn.execute(db.select([tracks]))
xx = tt.fetchall()

For testing - this script contributes nothing else but the ability to test sqlalchemy queries. 

metadata = db.MetaData()

albums = db.Table('albums', metadata, autoload=True, autoload_with=engine)

tt = conn.execute(db.select([albums.Title]))
xx = tt.fetchall()



Build the query below in sqlalchemy 

select 
                          t.Name as TrackName
                        , t.Composer as Composer
                        , t.Milliseconds as Milliseconds
                        , a.Title as AlbumTitle
                        , g.Name as Genre
                        from 
                          tracks as t
                        left join albums as a
                          on a.AlbumId = t.AlbumId
                        left join genres as g
                          on g.GenreId = t.GenreId
"""