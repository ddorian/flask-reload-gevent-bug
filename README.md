# flask-reload-gevent-bug


OS: Ubuntu 22.04.5 LTS

Run the app:
```bash
❯ python main.py
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 685-310-303
```
Then make a change on the file, save the file, and it will try to restart and crash:
```
 * Detected change in '/home/guru/Desktop/flask-reload-gevent-bug/main.py', reloading
python: /tmp/build/gevent/deps/libev/ev_epoll.c:134: epoll_modify: Assertion `("libev: I/O watcher with invalid fd found in epoll_ctl", (*__errno_location ()) != 9 && (*__errno_location ()) != 40 && (*__errno_location ()) != 22)' failed.
```
