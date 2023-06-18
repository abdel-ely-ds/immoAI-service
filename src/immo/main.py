import uvicorn

entry_point = "immo.app:app"


def main():
    uvicorn.run(entry_point, host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
