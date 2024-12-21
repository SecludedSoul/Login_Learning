def err(b):
    try:
        a= 5
        if b <0:
            raise ValueError("Cannot Division By Minus Value")
        print(a/b)
    except Exception as e:
        print(e)
err(-10)