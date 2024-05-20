from view import RealTimeServiceASGI

def main():
    asgi = RealTimeServiceASGI()
    asgi.run_server()

if __name__ == "__main__":
    main()