import tabs_app
import config

if __name__ == "__main__":
    config.dashApp.layout = tabs_app.tabstripPage()
    config.dashApp.run_server(debug=False)
