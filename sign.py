from app import app, rdb

@app.shell_context_processor
def make_shell_context():
    return {'rdb': rdb}
