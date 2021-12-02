from app import app, db

if __name__ == '__main__':
    # app.run(port=5000)
    db.drop_all()
    db.create_all()
