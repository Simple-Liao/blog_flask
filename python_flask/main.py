from python_flask.app.route import app

if __name__ == '__main__':
    app.logger.info('---开始记录---')
    app.run(debug=True)
    app.logger.info('---记录完成---')