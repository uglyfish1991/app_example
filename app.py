from website import create_app
#imports the whole website folder, and the create_app() from __init__.py

app = create_app() # the returned object from create_app() with all the config in

if __name__ == "__main__":
    app.run(debug=True)