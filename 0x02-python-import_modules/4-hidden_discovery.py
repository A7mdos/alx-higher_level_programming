#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    namespace = dir(hidden_4)
    for name in namespace:
        if name[0:2] != "__":
            print(name)
