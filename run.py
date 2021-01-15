from app import app

if __name__ == '__main__':
    # Debugger is active. Don't need to restart every time if there are changes.
    app.run(debug=True, host='0.0.0.0', port=3000)

